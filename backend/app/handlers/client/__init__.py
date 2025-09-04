from fastapi import APIRouter
from .asr import router as asr_router

router = APIRouter(prefix="/api/client")
router.include_router(asr_router)
