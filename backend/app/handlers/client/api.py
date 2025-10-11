from fastapi import APIRouter, Request
from ...mods import Types

router = APIRouter(prefix="/types")


@router.post("")
async def all(request: Request):
    types = await Types.all().order_by("-id")
    return {"success": True, "message": "获取语音成功", "data": types}


@router.post("/get")
async def get(request: Request):
    data = await request.json()
    id = data.get("id")
    type = await Types.get_or_none(id=id)
    return {"success": True, "message": "获取语音成功", "data": type}


@router.post("/add")
async def add(request: Request):
    data = await request.json()
    name = data.get("name")
    content = data.get("content")
    type = Types(name=name, content=content)
    await type.save()
    return {"success": True, "message": "获取语音成功", "data": type}


@router.post("/update")
async def update(request: Request):
    data = await request.json()
    id = data.get("id")
    name = data.get("name")
    content = data.get("content")
    type = await Types.get_or_none(id=id)
    type.name = name
    type.content = content
    await type.save()
    types = await Types.all().order_by("-id")
    return {"success": True, "message": "删除语音成功", "data": types}


@router.post("/delete")
async def delete(request: Request):
    data = await request.json()
    id = data.get("id")
    type = await Types.get_or_none(id=id)
    await type.delete()
    types = await Types.all().order_by("-id")
    return {"success": True, "message": "删除语音成功", "data": types}
