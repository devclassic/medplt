from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from ...utils.http import http
import os

router = APIRouter(prefix="/check")


@router.post("")
async def check(request: Request):
    data = await request.json()
    type = data.get("type")
    content = data.get("content")
    baseapi = os.getenv("BASE_API")
    url = f"{baseapi}/workflows/run"
    token = os.getenv("TOKEN_NEIHANZHIKONG")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = {
        "inputs": {
            "type": type,
            "content": content,
        },
        "response_mode": "streaming",
        "user": "demo",
    }

    async def event_stream():
        async with http.stream("POST", url, json=data, headers=headers) as res:
            async for chunk in res.aiter_bytes():
                yield chunk

    return StreamingResponse(event_stream(), media_type="text/event-stream")
