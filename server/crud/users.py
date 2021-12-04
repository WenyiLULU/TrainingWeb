from sqlalchemy.orm import Session

from server.models.Users import User
from server.schemas.User import UserCreate
from server.security.security import hash_password


def read_users(db: Session, offset: int = 0, limit: int = 100):
    return db.query(User).offset(offset).limit(limit).all()  # db_users[offset:offset+limit]


def read_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()  # db_users[user_id]


def read_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()  # db_users[user_id]


def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, password=hash_password(user.password), is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
