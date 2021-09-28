from pydantic import BaseModel, ValidationError
from typing import List, Optional


# ================ Diary ================

class PageBase(BaseModel):
    diaryId: int
    pageTitle : str
    pageContent : str
    pageShare : bool
    pageDiaryId : str
    pageOwnerId : str
    pageImage : str
    top : float
    left : float

class PageCreate(PageBase):
    class Config:
        orm_mode = True


class PageUpdateFrom(BaseModel):
    diaryId: int
    modifyName: str


class PageDeleteForm(BaseModel):
    diaryId: int


class Page(PageBase):
    id: int
    pageDiary : str

    class Config:
        orm_mode = True
