from transformers import (
    AutoProcessor,
    AutoModelForImageTextToText,
    TextIteratorStreamer,
)
from transformers.generation.streamers import BaseStreamer
from threading import Thread
import torch
import json
import asyncio

from queue import Queue, Empty
import asyncio

class AsyncIteratorStreamer(BaseStreamer):
    def __init__(self, tokenizer, skip_prompt=True, skip_special=False):
        self.tokenizer = tokenizer
        self.skip_prompt = skip_prompt
        self.skip_special = skip_special
        self.q = Queue()          # 同步队列
        self.prompt_skipped = False
        self.finish = False

    def put(self, value):
        if self.skip_prompt and not self.prompt_skipped:
            self.prompt_skipped = True
            return
        text = self.tokenizer.decode(value, skip_special_tokens=self.skip_special)
        if text:
            self.q.put(text)

    def end(self):
        self.q.put(None)          # 结束标志

    # --- 下面让 FastAPI 能 async for ---
    def __aiter__(self):
        return self

    async def __anext__(self):
        while True:
            try:
                # 用 to_thread 把阻塞 get 丢到线程池
                val = await asyncio.to_thread(self.q.get, timeout=0.1)
            except Empty:
                continue
            if val is None:
                raise StopAsyncIteration
            return val





class Medgemma:
    def init(self):
        self.model_id = "models/medgemma-4b-it"
        self.model = AutoModelForImageTextToText.from_pretrained(
            self.model_id,
            dtype=torch.bfloat16,
            device_map="auto",
        )
        self.processor = AutoProcessor.from_pretrained(self.model_id, use_fast=True)
        self.tokenizer = self.processor.tokenizer

    async def generate(self, messages):
        inputs = self.processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt"
        ).to(self.model.device, dtype=torch.bfloat16)

        streamer = AsyncIteratorStreamer(self.tokenizer, skip_prompt=True, skip_special=True)

        gen_kwargs = dict(
            **inputs,
            streamer=streamer,
            max_new_tokens=4096,
            do_sample=False,
            use_cache=True,
            pad_token_id=self.tokenizer.eos_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
        )

        Thread(target=self.model.generate, kwargs=gen_kwargs, daemon=True).start()

        async for token in streamer:
            print(token)
            yield f"data: {json.dumps({'event':'message','token':token})}\n\n"

        yield f"data: {json.dumps({'event':'message_end'})}\n\n"