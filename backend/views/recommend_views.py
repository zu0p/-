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

logger = logging.getLogger()
logger.setLevel(logging.INFO)

recommend_router = APIRouter()

# ================================== diary CRUD ==================================

### C
@recommend_router.get("/recommend_by_page/{pageId}")
async def create_diary( pageId: int ):
    new_diary = diary_crud.create_diary(db, diary_data, current_user.userId)
    return new_diary



