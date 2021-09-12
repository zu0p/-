from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from database import get_db

from schemas import user_schemas # schemas
from models import user_model # models
from crud import user_crud # crud

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

@user_router.get("/users/me/", response_model=user_schemas.UserInDB)
async def read_users_me(current_user: user_schemas.UserInDB = Depends(user_crud.get_current_active_user)):
    return current_user

# ================================== user CRUD ==================================
@user_router.post("/signup", response_model=user_schemas.UserInDB)
def sign_up(user_data: user_schemas.UserInDB, db: Session = Depends(get_db)): # DI
    new_user = user_crud.create_user(db, user_data)
    return new_user
