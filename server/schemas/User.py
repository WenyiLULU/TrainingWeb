from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field("username", title="This is the user's name, to identify it.", min_length=5)
    is_admin: Optional[bool] = False


class UserCreate(UserBase):
    password: str = Field("password", min_length=8)


class User(UserBase):

    class Config:
        orm_mode = True
