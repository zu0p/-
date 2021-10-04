
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
import pandas as pd
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import create_engine

# aws
db_user = "test"
db_password = "test"
db_name = "ssafy_fastapi_web"
db_server = "j5d103.p.ssafy.io:3306"

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_server}/{db_name}"
#SQLALCHEMY_DATABASE_URL = os.environ['SQLALCHEMY_DB_URL']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

conn = engine.connect()

# ============================ music recommend data return ============================

### return all data in pandas object
def return_musics_in_pdObject():
    data = pd.read_sql_table('music_info', conn)
    # print(data.head())
    return data