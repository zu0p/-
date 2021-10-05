import os
import asyncio
import aiofiles
import logging
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, status, FastAPI, File, Form, UploadFile
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from database import get_db

from schemas import user_schemas # schemas
from models import user_model # models
from crud import user_crud # crud

# image S3
from utils.image_upload import client_s3, upload_file

# 로그 생성
logger = logging.getLogger()
# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

user_router = APIRouter()

# ================================== user Auth ==================================

@user_router.post("/login", response_model=user_schemas.Token)
async def login_for_access_token(form_data: user_schemas.UserLoginForm, db: Session = Depends(get_db)): # DI
    user = user_crud.authenticate_user(db, form_data.userId, form_data.userPwd)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect userId or userPwd",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=user_crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user_crud.create_access_token(
        data={"sub": user.userId}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



# ================================== user CRUD ==================================

### C
@user_router.post("/signup", response_model=user_schemas.UserInDB)
async def create_user(user_data: user_schemas.UserInDB, db: Session = Depends(get_db)): # DI
    new_user = user_crud.create_user(db, user_data)
    return new_user

### R
@user_router.get("/me", response_model=user_schemas.UserInDB)
async def read_user_one(current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    return current_user

### U
@user_router.put("/update", response_model=user_schemas.UserInDB)
async def update_user(user_data: user_schemas.UserUpdate, db: Session = Depends(get_db), 
                        old_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    updated_user = user_crud.update_user(db, user_data, old_user)
    return updated_user

### D
@user_router.delete("/delete")
async def update_user(current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user), db: Session = Depends(get_db)):
    user_crud.delete_user(db, current_user)
    return {"state": "success"}

# ================================== user ETC ==================================

### 아이디 중복확인
@user_router.post("/checkDuplication")
def duplication_user(inputUser: user_schemas.checkDuplication, db: Session = Depends(get_db)):
    if user_crud.duplicate_user(db, inputUser):
        return {"state": "yes"} 
    return {"state": "no"} 

### 비밀번호 변경
@user_router.put("/change-password")
def change_password(newPassword: user_schemas.changePassword, db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    user_crud.change_password(db, current_user, newPassword)
    return {"state": "success"}

### 프로필 이미지 변경
@user_router.put("/change-image")
async def change_image(
                        profileImage: UploadFile = File(...),
                        db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    # image 저장부분
    UPLOAD_DIRECTORY = "./static/image/profile/"
    file_name = current_user.userId+".jpg"
    new_path = os.path.join(UPLOAD_DIRECTORY, file_name)
    async with aiofiles.open(new_path, "wb") as fp:
        # async read
        contents = await profileImage.read()  
        # async write
        await fp.write(contents)
        # aws image upload
        # profile -> userId.jpeg
        # diary -> userId_diaryId.jpeg
        # page -> userId_diaryId_pageId.jpeg
        await upload_file(UPLOAD_DIRECTORY+file_name,
                "profile/"+file_name, 
                client_s3)
    fp.close()

    logger.info(profileImage)
    changed_url = user_crud.change_image(db, current_user, new_path)
    return {"state": "success", "changedImg": changed_url}
