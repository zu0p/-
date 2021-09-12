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



# ================================== user CRUD ==================================

### C
@user_router.post("/signup", response_model=user_schemas.UserInDB)
async def create_user(user_data: user_schemas.UserInDB, db: Session = Depends(get_db)): # DI
    new_user = user_crud.create_user(db, user_data)
    return new_user

### R
@user_router.get("/me", response_model=user_schemas.UserInDB)
async def read_user_one(current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    return current_user

### U
@user_router.put("/update", response_model=user_schemas.UserInDB)
def update_user(user_data: user_schemas.UserUpdate, db: Session = Depends(get_db), 
                        old_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    updated_user = user_crud.update_user(db, user_data, old_user)
    return updated_user

### D
@user_router.delete("/delete")
def update_user(current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user), db: Session = Depends(get_db)):
    user_crud.delete_user(db, current_user)
    return {"state": "success"}