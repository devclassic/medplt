from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import StreamingResponse
from ...models.asr import Asr
import os
import uuid
import shutil
import anyio
from ...utils.http import http

model = Asr()
model.init()

router = APIRouter(prefix="/asr")


@router.post("")
async def asr(file: UploadFile = File()):
    basepath = "public/uploads/asr/"
    if not os.path.exists(basepath):
        os.makedirs(basepath)
    ext = os.path.splitext(file.filename)[1]
    filename = basepath + str(uuid.uuid4()) + ext
    with open(filename, "wb") as f:
        shutil.copyfileobj(file.file, f)
    res = await anyio.to_thread.run_sync(model.generate, filename)
    return {"success": True, "message": "语音识别成功", "data": res}


@router.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    baseapi = os.getenv("BASE_API")
    url = f"{baseapi}/chat-messages"
    token = os.getenv("TOKEN_DUIHUASHENGCHENG")
    headers = {
        "Authorization": f"Bearer {token}",
    }
    data = {
        "user": "demo",
        "inputs": {},
        "query": prompt,
        "response_mode": "streaming",
    }

    async def event_stream():
        async with http.stream("POST", url, json=data, headers=headers) as res:
            async for chunk in res.aiter_bytes():
                yield chunk

    return StreamingResponse(event_stream(), media_type="text/event-stream")
