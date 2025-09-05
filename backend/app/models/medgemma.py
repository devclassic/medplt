from transformers import (
    AutoProcessor,
    AutoModelForImageTextToText,
    TextIteratorStreamer,
)
from threading import Thread
import torch
import json


class Medgemma:
    def init(self):
        self.model_id = "models/medgemma-4b-it"
        self.model = AutoModelForImageTextToText.from_pretrained(
            self.model_id,
            dtype=torch.bfloat16,
            device_map="auto",
        )
        self.processor = AutoProcessor.from_pretrained(self.model_id, use_fast=True)

    def generate(self, messages):
        inputs = self.processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(self.model.device, dtype=torch.bfloat16)

        streamer = TextIteratorStreamer(
            self.processor.tokenizer,
            skip_prompt=True,
            skip_special_tokens=True,
        )

        generation_kwargs = dict(
            **inputs,
            streamer=streamer,
            max_new_tokens=8192,
            do_sample=False,
        )

        Thread(
            target=self.model.generate, kwargs=generation_kwargs, daemon=True
        ).start()

        for token in streamer:
            if token:
                yield f"data: {json.dumps({'event':'message','token': token})}\n\n"
        yield f"data: {json.dumps({'event':'message_end'})}\n\n"
