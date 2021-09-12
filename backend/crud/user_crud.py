

from database import get_db
from typing import Optional
from schemas.user_schemas import TokenData, UserInDB
from fastapi import APIRouter, HTTPException, Depends, status
from database import SessionLocal
from datetime import datetime, timedelta
from jose import JWTError, jwt
from models import user_model
from schemas import user_schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



# ============================ user Auth ============================

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "a6480a82721880f4cebcd01f4963f65e126fdf0c15292b3817cac34c7198bad5"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호 확인
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 비밀번호 hash
def get_password_hash(password):
    return pwd_context.hash(password)

# access-token 발급
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 유저 반환
def get_user(db: SessionLocal, userId: str):
    return db.query(user_model.UserInfo).filter(user_model.UserInfo.userId == userId).first()

# 유저 확인
def authenticate_user(db: SessionLocal, userId: str, userPwd: str):
    user = get_user(db, userId)
    if not user:
        return False
    if not verify_password(userPwd, user.userPwd):
        return False
    return user

# 현재 유저 반환
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        userId: str = payload.get("sub")
        if userId is None:
            raise credentials_exception
        token_data = TokenData(userId=userId)
    except JWTError:
        raise credentials_exception
    user = get_user(db, userId=token_data.userId)
    if user is None:
        raise credentials_exception
    return user



# ============================ user CRUD ============================
### C
def create_user(db: SessionLocal, user_data: user_schemas.UserInDB):
    db_user = user_model.UserInfo(
        userId = user_data.userId,
        userPwd = get_password_hash(user_data.userPwd),
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

### U
def update_user(db: SessionLocal, user_data: user_schemas.UserUpdate, old_user:user_schemas.UserInDB):
    old_user.userName = user_data.userName
    old_user.userEmail = user_data.userEmail
    old_user.userNick = user_data.userNick
    old_user.userPhone = user_data.userPhone
    db.commit()
    db.refresh(old_user)
    return old_user

### D
def delete_user(db: SessionLocal, user_data: user_schemas.UserInDB):
    db.delete(user_data)
    db.commit()
    return