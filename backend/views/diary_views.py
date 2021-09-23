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

# 로그 생성
logger = logging.getLogger()
# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

diary_router = APIRouter()

# ================================== diary CRUD ==================================

### C
@diary_router.post("/create", response_model=diary_schemas.DiaryCreate)
async def create_diary(
                        diaryName: str = Form(...),
                        diaryImage: UploadFile = File(...),
                        diaryDesc: str = Form(...),
                        diaryShare: bool = Form(...),
                        db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    # image 저장부분
    UPLOAD_DIRECTORY = "./static/image/diary/"
    new_path = os.path.join(UPLOAD_DIRECTORY, current_user.userId+f"_{diaryName}.jpg")
    async with aiofiles.open(new_path, "wb") as fp:
        contents = await diaryImage.read()  # async read
        fp.write(contents)
        await fp.write(contents)  # async write
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


### R
@diary_router.get("/read")
async def read_diary(
                        db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    read_diaries = diary_crud.read_diary(db, current_user.userId)
    return read_diaries


### U
@diary_router.put("/update")
async def update_diary(
                        updateInfo: diary_schemas.DiaryUpdateFrom,
                        db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    diary_crud.update_diary(db, current_user.userName, updateInfo)
    return {"state": "success"}


### D
@diary_router.delete("/delete")
async def delete_diary(
                        deleteInfo: diary_schemas.DiaryDeleteForm,
                        db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    diary_crud.delete_diary(db, current_user.userName, deleteInfo.diaryId)
    return {"state": "success"}


