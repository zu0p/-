
from typing import List

from pydantic import BaseModel
from pydantic import EmailStr

# Login
class UserLoginReq(BaseModel):
    userId : str
    userPwd : str


class UserBase(BaseModel):
    userId : str
    userName : str
    userEmail : EmailStr
    userNick : str
    userPhone : str
    userImage : str


class UserCreate(UserBase):
    userPwd : str
    
    class Config:
        orm_mode = True

class User(UserBase):
    id: int

    class Config:
        orm_mode = True # Pydantic's orm_mode will tell the Pydantic model to read the data 
                        # even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
                        # id = data["id"] 뿐 아니라 id = data.id로도 가능해짐!

