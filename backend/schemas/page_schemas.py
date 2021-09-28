from pydantic import BaseModel, ValidationError
from typing import List, Optional


# ================ Diary ================

class PageBase(BaseModel):
    diaryId: int
    pageTitle : str
    pageContent : str
    pageShare : bool
    pageImage : str
    top : float
    left : float

class PageCreate(PageBase):
    pageOwnerId : str
    class Config:
        orm_mode = True


class PageUpdateFrom(PageBase):
    pageId: int
    class Config:
        orm_mode = True


class PageDeleteForm(BaseModel):
    diaryId: int


class Page(PageBase):
    id: int
    pageOwnerId : str
    class Config:
        orm_mode = True
