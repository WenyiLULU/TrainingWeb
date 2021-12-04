from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from server.crud.users import read_users, read_user_by_id, read_user_by_username, create_user
from server.db.db import get_db
from server.schemas.User import User, UserCreate


router = APIRouter()


@router.get("/", response_model=List[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return read_users(db=db, offset=skip, limit=limit)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = read_user_by_id(user_id=user_id, db=db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/", response_model=User)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    if read_user_by_username(db=db, username=user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    return create_user(db=db, user=user)
