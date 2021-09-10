from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from database import get_db
# schemas
from schemas import user_schemas
# models
from models import user_model
# crud
from crud import user_crud

user_router = APIRouter()

@user_router.post("/signup", response_model=user_schemas.UserCreate)
def sign_up(user_data: user_schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = user_crud.create_user(db, user_data)
    return new_user