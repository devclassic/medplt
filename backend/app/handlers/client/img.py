from typing import List
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import StreamingResponse
import os
import shutil
import uuid
from ...utils.http import http


router = APIRouter(prefix="/img")


@router.post("")
async def images(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    history = data.get("history", "")
    imgs = data.get("imgs", [])

    baseapi = os.getenv("BASE_API")
    url = f"{baseapi}/files/upload"
    token = os.getenv("TOKEN_TUXIANGSHIBIE")
    headers = {
        "Authorization": f"Bearer {token}",
    }
    data = {"user": "demo"}

    pics = []
    for img in imgs:
        with open(img, "rb") as f:
            r = await http.post(
                url,
                headers=headers,
                data=data,
                files={"file": (os.path.basename(img), f)},
            )
            pics.append(r.json()["id"])

    url = f"{baseapi}/chat-messages"

    data = {
        "inputs": {},
        "query": prompt,
        "response_mode": "streaming",
        "user": "demo",
        "files": [
            {
                "type": "image",
                "transfer_method": "local_file",
                "upload_file_id": id,
            }
            for id in pics
        ],
    }

    async def event_stream():
        async with http.stream("POST", url, json=data, headers=headers) as res:
            async for chunk in res.aiter_bytes():
                yield chunk

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@router.post("/upimg")
async def upimg(files: List[UploadFile] = File([])):
    images = []
    basepath = "public/uploads/image/"
    if not os.path.exists(basepath):
        os.makedirs(basepath)
    for file in files:
        ext = os.path.splitext(file.filename)[1]
        filename = basepath + str(uuid.uuid4()) + ext
        with open(filename, "wb") as f:
            shutil.copyfileobj(file.file, f)
            images.append(filename)
    return {"success": True, "message": "上传图片成功", "data": images}
