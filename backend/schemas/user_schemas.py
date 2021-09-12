
from typing import List, Optional

from pydantic import BaseModel
from pydantic import EmailStr

# ================ Token ================

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    userId: Optional[str] = None



# ================ Login ================

class UserLoginForm(BaseModel):
    userId: str
    userPwd: str



# ================ User ================

class UserBase(BaseModel):
    userId : str
    userName : str
    userEmail : EmailStr
    userNick : str
    userPhone : str
    userImage : str


class UserInDB(UserBase):
    userPwd : str
    
    class Config:
        orm_mode = True

class User(UserBase):
    id: int

    class Config:
        orm_mode = True # Pydantic's orm_mode will tell the Pydantic model to read the data 
                        # even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
                        # id = data["id"] 뿐 아니라 id = data.id로도 가능해짐!

class UserUpdate(BaseModel):
    userName: str
    userEmail: str
    userNick: str
    userPhone: str
