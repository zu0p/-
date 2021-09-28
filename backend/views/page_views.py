import os
import asyncio
import aiofiles
import logging
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, status, FastAPI, File, Form, UploadFile
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.sql.sqltypes import Integer

from database import get_db

from schemas import page_schemas, user_schemas, diary_schemas # schemas
from models import user_model, diary_model # models
from crud import user_crud, diary_crud, page_crud # crud

# image S3
from utils.image_upload import client_s3, upload_file

# 로그 생성
logger = logging.getLogger()
# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

page_router = APIRouter()

# ================================== page CRUD ==================================

### C
@page_router.post("/create")
async def create_page(
                        diaryId: int = Form(...),
                        pageTitle: str = Form(...),
                        pageContent: str = Form(...),
                        pageShare: bool = Form(...),
                        pageImage: UploadFile = File(...),
                        top: float = Form(...),
                        left: float = Form(...),
                        
                        db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    # image 저장부분
    UPLOAD_DIRECTORY = "./static/image/page/"
    file_name = f"{current_user.userId}_"+str(diaryId)+f"_{pageTitle}.jpg"
    new_path = os.path.join(UPLOAD_DIRECTORY, file_name)
    async with aiofiles.open(new_path, "wb") as fp:
        # async read
        contents = await pageImage.read()  
        # async write
        await fp.write(contents) 
        # aws image upload
        # profile -> userId.jpeg
        # diary -> userId_diaryId.jpeg
        # page -> userId_diaryId_pageId.jpeg
        await upload_file(UPLOAD_DIRECTORY+file_name,
                "page/"+file_name, 
                client_s3)
    fp.close()
    # diary create 객체생성
    page_data = page_schemas.PageCreate(
        diaryId = diaryId,
        pageTitle =  pageTitle,
        pageContent = pageContent,
        pageShare = pageShare,
        pageOwnerId = current_user.userId,
        pageImage = new_path,
        top = top,
        left = left
    )
    # db 저장부분
    new_page = page_crud.create_page(db, page_data, current_user.userId)
    return new_page


### R
# @page_router.get("/read")
# async def read_diary(
#                         db: Session = Depends(get_db),
#                         current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
#     read_diaries = diary_crud.read_diary(db, current_user.userId)
#     return read_diaries

# @page_router.get("/read/{diaryId}")
# async def read_diary(
#                         diaryId: str,
#                         db: Session = Depends(get_db),
#                         current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
#     read_diaries = diary_crud.read_one_diary(db, current_user.userId, diaryId)
#     return read_diaries


# ### U
# @page_router.put("/update")
# async def update_diary(
#                         updateInfo: diary_schemas.DiaryUpdateFrom,
#                         db: Session = Depends(get_db),
#                         current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
#     diary_crud.update_diary(db, current_user.userId, updateInfo)
#     return {"state": "success"}


# ### D
# @page_router.delete("/delete")
# async def delete_diary(
#                         deleteInfo: diary_schemas.DiaryDeleteForm,
#                         db: Session = Depends(get_db),
#                         current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
#     diary_crud.delete_diary(db, current_user.userId, deleteInfo.diaryId)
#     return {"state": "success"}


