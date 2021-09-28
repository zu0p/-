
from sqlalchemy.sql.sqltypes import Integer
from database import get_db
from typing import Optional
from schemas.user_schemas import TokenData, UserInDB
from fastapi import APIRouter, HTTPException, Depends, status, FastAPI, File, Form, UploadFile
from database import SessionLocal
from datetime import datetime, timedelta
from jose import JWTError, jwt
from models import diary_model, user_model, page_model
from schemas import page_schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# ============================ page CRUD ============================

### C
def create_page(db: SessionLocal, page_data: page_schemas.PageBase, owner: str):
    Base_url = "https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/"
    db_page = page_model.PageInfo(
        diaryId = page_data.diaryId,
        pageTitle = page_data.pageTitle,
        pageContent = page_data.pageContent,
        pageShare = page_data.pageShare,
        pageOwnerId = owner,
        pageImage = Base_url + f"page/{owner}_{page_data.diaryId}_{page_data.pageTitle}.jpg",
        top = page_data.top,
        left = page_data.left
    )
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page

### R
def read_pagies(db: SessionLocal, owner: str, diaryId: str, skip: int = 0, limit: int = 100):
    return db.query(page_model.PageInfo).filter_by(diaryId=diaryId).offset(skip).limit(limit).all()

def read_one_page(db: SessionLocal, owner: str, diaryId:str, pageId:str, skip: int = 0, limit: int = 100):
    return db.query(page_model.PageInfo).filter_by(diaryId=diaryId).filter_by(id=pageId).first()


### U
def update_page(db: SessionLocal, owner: str, updateInfo:page_schemas.PageUpdateFrom):
    Base_url = "https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/"
    get = db.query(page_model.PageInfo).filter_by(id=updateInfo.pageId).first()
    get.diaryId=updateInfo.diaryId
    get.pageTitle=updateInfo.pageTitle
    get.pageContent=updateInfo.pageContent
    get.pageShare=updateInfo.pageShare
    get.pageImage=Base_url + f"page/{owner}_{updateInfo.diaryId}_{updateInfo.pageTitle}.jpg"
    get.top=updateInfo.top
    get.left=updateInfo.left
    db.commit()
    return 

### D
def delete_page(db: SessionLocal, owner: str, deleteInfo: page_schemas.PageDeleteForm):
    db.query(page_model.PageInfo).filter_by(diaryId=deleteInfo.diaryId).filter_by(id=deleteInfo.pageId).delete()
    db.commit()
    return 