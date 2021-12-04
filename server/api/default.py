from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {"res": "Hello !"}


@router.get("/hi")
def hello(name: str = ""):
    return {"res": f"Hello {name}!"}
