from typing import List
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import StreamingResponse
import os
import shutil
import uuid
import json
from ...models.medgemma import Medgemma
import glob
import dicom2jpg


model = Medgemma()
model.init()

router = APIRouter(prefix="/image")


@router.post("")
async def images(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    history = data.get("history", "")
    imgs = data.get("imgs", [])

    messages = history
    msg = {"role": "user", "content": []}
    for img in imgs:
        msg["content"].append({"type": "image", "image": img})
    msg["content"].append({"type": "text", "text": prompt})
    messages.append(msg)

    return StreamingResponse(
        model.generate(messages),
        media_type="text/event-stream",
    )


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


@router.post("/updcm")
async def updcm(files: List[UploadFile] = File([])):
    basedir = "public/uploads/dcm/"
    rd = str(uuid.uuid4())
    updir = basedir + "endcm_" + rd + "/"
    downdir = basedir + "dedcm_" + rd + "/"
    os.path.exists(updir) or os.makedirs(updir)

    for file in files:
        filename = updir + file.filename + ".dcm"
        with open(filename, "wb") as f:
            shutil.copyfileobj(file.file, f)

    try:
        dicom2jpg.dicom2png(origin=updir, target_root=downdir, multiprocessing=False)
        paths = glob.glob(downdir + "**/*.png", recursive=True)
        images = []
        for path in paths:
            images.append(path.replace("\\", "/").replace("public/", "/"))
        return {
            "success": True,
            "message": "上传DCM成功",
            "data": {"images": images, "imgs": paths},
        }
    except:
        return {"success": False, "message": "处理DCM失败"}
