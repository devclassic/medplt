from fastapi import APIRouter
from .asr import router as asr_router
from .check import router as check_router

router = APIRouter(prefix="/api/client")
router.include_router(asr_router)
router.include_router(check_router)
