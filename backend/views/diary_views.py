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

# 로그 생성
logger = logging.getLogger()
# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

diary_router = APIRouter()

# ================================== diary CRUD ==================================

### C
@diary_router.post("/create")
async def create_diary(
                    diaryImage: UploadFile = File(...),
                    db: Session = Depends(get_db),
                    current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    # image 저장부분
    UPLOAD_DIRECTORY = "./static/image/diary/"
    new_path = os.path.join(UPLOAD_DIRECTORY, current_user.userId+".jpg")
    async with aiofiles.open(new_path, "wb") as fp:
        contents = await diaryImage.read()  # async read
        fp.write(contents)
        await fp.write(contents)  # async write
    fp.close()


    pass

# @user_router.post("/signup", response_model=user_schemas.UserInDB)
# async def create_user(user_data: user_schemas.UserInDB, db: Session = Depends(get_db)): # DI
#     new_user = user_crud.create_user(db, user_data)
#     return new_user

# ### R
# @user_router.get("/me", response_model=user_schemas.UserInDB)
# async def read_user_one(current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
#     return current_user

# ### U
# @user_router.put("/update", response_model=user_schemas.UserInDB)
# async def update_user(user_data: user_schemas.UserUpdate, db: Session = Depends(get_db), 
#                         old_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
#     updated_user = user_crud.update_user(db, user_data, old_user)
#     return updated_user

# ### D
# @user_router.delete("/delete")
# async def update_user(current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user), db: Session = Depends(get_db)):
#     user_crud.delete_user(db, current_user)
#     return {"state": "success"}

