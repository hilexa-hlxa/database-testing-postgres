from models import User
from sqlalchemy.orm import Session
from schemas import UserCreate

def create_user(db: Session, data: UserCreate):
    user_instance = User(**data.model_dump())
    db.add(user_instance)
    db.commit()
    db.refresh(instance=user_instance)
    return user_instance

def get_user(db: Session):
    return db.query(User).all()

def get_user_byid(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user: UserCreate, user_id: int):
    user_queryset = db.query(User).filter(User.id == user_id).first()
    if user_queryset:
        for key, value in user.model_dump().items():
            setattr(user_queryset, key, value)
        db.commit()
        db.refresh(user_queryset)
        return user_queryset

def delete_user(db: Session, user_id: int):
    user_queryset = db.query(User).filter(User.id == user_id).first()
    if user_queryset:
        db.delete(user_queryset)
        db.commit()
    return user_queryset

