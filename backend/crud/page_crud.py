
from sqlalchemy.sql.sqltypes import Integer
from database import get_db
from typing import Optional
from schemas.user_schemas import TokenData, UserInDB
from fastapi import APIRouter, HTTPException, Depends, status, FastAPI, File, Form, UploadFile
from database import SessionLocal
from datetime import datetime, timedelta
from jose import JWTError, jwt
from models import diary_model, user_model, page_schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# ============================ page CRUD ============================

### C
def create_page(db: SessionLocal, page_data: page_schemas.PageBase, owner: str):
    Base_url = "https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/"
    db_diary = diary_model.DiaryInfo(
        diaryName = diary_data.diaryName,
        diaryImage = Base_url + f"page/{owner}_{page_data.diaryId}_{page_data.pageTitle}.jpg",
        diaryDesc = diary_data.diaryDesc,
        diaryShare = diary_data.diaryShare,
        diaryOwnerId = owner
    )
    db.add(db_diary)
    db.commit()
    db.refresh(db_diary)
    return db_diary

### R
def read_diary(db: SessionLocal, owner: str, skip: int = 0, limit: int = 100):
    return db.query(diary_model.DiaryInfo).filter_by(diaryOwnerId=owner).offset(skip).limit(limit).all()

def read_one_diary(db: SessionLocal, owner: str, diaryId:str, skip: int = 0, limit: int = 100):
    return db.query(diary_model.DiaryInfo).filter_by(diaryOwnerId=owner).filter_by(id=diaryId).first()


### U
def update_diary(db: SessionLocal, owner: str, updateInfo:diary_schemas.DiaryUpdateFrom):
    get = db.query(diary_model.DiaryInfo).filter_by(diaryOwnerId=owner).filter_by(id=updateInfo.diaryId).first()
    get.diaryName=updateInfo.modifyName
    db.commit()
    return 

### D
def delete_diary(db: SessionLocal, owner: str, diaryId: Integer):
    db.query(diary_model.DiaryInfo).filter_by(diaryOwnerId=owner).filter_by(id=diaryId).delete()
    db.commit()
    return 