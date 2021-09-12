from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from database import get_db

from schemas import user_schemas # schemas
from models import user_model # models
from crud import user_crud # crud

user_router = APIRouter()

# user Auth
@user_router.post("/login")
def login(login_data: user_schemas.UserLoginReq):
    print(login_data)
    return {"access_token": login_data.userId, "token_type": login_data.userPwd}




# user CRUD

@user_router.post("/signup", response_model=user_schemas.UserInDB)
def sign_up(user_data: user_schemas.UserInDB, db: Session = Depends(get_db)):
    new_user = user_crud.create_user(db, user_data)
    return new_user
