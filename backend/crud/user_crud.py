

from database import SessionLocal
from models import user_model
from schemas import user_schemas

def create_user(db: SessionLocal, user_data: user_schemas.UserCreate):
    db_user = user_model.UserInfo(
        userId = user_data.userId,
        userPwd = user_data.userPwd,
        userName = user_data.userName,
        userEmail = user_data.userEmail,
        userNick = user_data.userNick,
        userPhone = user_data.userPhone,
        userImage = user_data.userImage
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
