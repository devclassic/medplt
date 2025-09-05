from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from ...utils.http import http
import os

router = APIRouter(prefix="/assist")


@router.post("")
async def assist(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    baseapi = os.getenv("BASE_API")
    url = f"{baseapi}/chat-messages"
    token = os.getenv("TOKEN_FUZHUZHENLIAO")
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
