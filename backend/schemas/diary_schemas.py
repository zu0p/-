from pydantic import BaseModel, ValidationError
from typing import List, Optional


# ================ Diary ================

class DiaryBase(BaseModel):
    diaryName : str
    diaryImage : str
    diaryDesc : str
    diaryShare : bool 


class DiaryCreate(DiaryBase):
    class Config:
        orm_mode = True


class DiaryUpdateFrom(BaseModel):
    diaryId: int
    modifyName: str


class DiaryDeleteForm(BaseModel):
    diaryId: int


class Diary(DiaryBase):
    id: int
    diaryOwner : str

    class Config:
        orm_mode = True
