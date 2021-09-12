

from database import SessionLocal
from models import user_model
from schemas import user_schemas
from passlib.context import CryptContext

# ============================ user Auth ============================

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def get_password_hash(password):
    return pwd_context.hash(password)



# ============================ user CRUD ============================
def create_user(db: SessionLocal, user_data: user_schemas.UserInDB):
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
