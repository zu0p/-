from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, status, FastAPI, File, Form, UploadFile
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


from database import get_db

from schemas import user_schemas # schemas
from models import user_model # models
from crud import user_crud # crud

user_router = APIRouter()

# ================================== user Auth ==================================

@user_router.post("/login", response_model=user_schemas.Token, )
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
async def create_user(  userId: str = Form(...),
                        userName: str = Form(...),
                        userPwd: str = Form(...),
                        userEmail: str = Form(...),
                        userNick: str = Form(...),
                        userPhone: str = Form(...),
                        profileImage: UploadFile = File(...), # pydantic doesn't support UplodaFile type
                        db: Session = Depends(get_db)): # DI

    user_data = user_model.UserInfo(
        userId = userId,
        userPwd = userPwd,
        userName = userName,
        userEmail = userEmail,
        userNick = userNick,
        userPhone = userPhone,
        userImage = userImageUrl
    )
    print(user_data)
    print(profileImage)
    new_user = user_crud.create_user(db, user_data, profileImage)
    return new_user

### R
@user_router.get("/me", response_model=user_schemas.UserInDB)
async def read_user_one(current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    return current_user

### U
@user_router.put("/update", response_model=user_schemas.UserInDB)
async def update_user(user_data: user_schemas.UserUpdate, db: Session = Depends(get_db), 
                        old_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    updated_user = user_crud.update_user(db, user_data, old_user)
    return updated_user

### D
@user_router.delete("/delete")
async def update_user(current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user), db: Session = Depends(get_db)):
    user_crud.delete_user(db, current_user)
    return {"state": "success"}

# ================================== user ETC ==================================

### 아이디 중복확인
@user_router.post("/checkDuplication")
def duplication_user(inputUser: user_schemas.checkDuplication, db: Session = Depends(get_db)):
    if user_crud.duplicate_user(db, inputUser):
        return {"state": "yes"} 
    return {"state": "no"} 

### 비밀번호 변경
@user_router.put("/change-password")
def change_password(newPassword: user_schemas.changePassword, db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    user_crud.change_password(db, current_user, newPassword)
    return {"state": "success"}

### 프로필 이미지 변경
@user_router.put("/change-image")
def change_image(newImageUrl: user_schemas.changeProfile, db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    user_crud.change_image(db, current_user, newImageUrl)
    return {"state": "success"}