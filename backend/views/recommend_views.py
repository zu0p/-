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

from schemas import user_schemas
from schemas import diary_schemas # schemas
from models import user_model, diary_model # models
from crud import user_crud, diary_crud # crud

# image S3
from utils.image_upload import client_s3, upload_file

# 로그 생성
logger = logging.getLogger()
# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

recommend_router = APIRouter()

# ================================== recommend - music ==================================

### C
@recommend_router.post("/create")
async def create_diary(
                        diaryName: str = Form(...),
                        diaryImage: UploadFile = File(...),
                        diaryDesc: str = Form(...),
                        diaryShare: bool = Form(...),
                        db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    # image 저장부분
    UPLOAD_DIRECTORY = "./static/image/diary/"
    file_name = current_user.userId+f"_{diaryName}.jpg"
    new_path = os.path.join(UPLOAD_DIRECTORY, file_name)
    async with aiofiles.open(new_path, "wb") as fp:
        # async read
        contents = await diaryImage.read()  
        # async write
        await fp.write(contents) 
        # aws image upload
        # profile -> userId.jpeg
        # diary -> userId_diaryName.jpeg
        # page -> userId_diaryName_pageName.jpeg
        await upload_file(UPLOAD_DIRECTORY+file_name,
                "diary/"+file_name, 
                client_s3)
    fp.close()
    # diary create 객체생성
    diary_data = diary_schemas.DiaryCreate(
        diaryName = diaryName,
        diaryImage = new_path,
        diaryDesc = diaryDesc,
        diaryShare = diaryShare,
    )
    # db 저장부분
    new_diary = diary_crud.create_diary(db, diary_data, current_user.userId)
    return new_diary


