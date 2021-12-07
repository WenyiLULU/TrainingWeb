from fastapi import APIRouter

from server.settings.app import SETTINGS

router = APIRouter()


@router.get("/")
def home():
    return {"res": "Hello !"}


@router.get("/info")
async def info():
    return {
        "app_name": SETTINGS.app_name,
        "admin_email": SETTINGS.admin_email
    }


@router.get("/hi")
def hello(name: str = ""):
    return {"res": f"Hello {name}!"}
