from sqlalchemy import Column,String,Boolean
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.sql.schema import ForeignKey

from database import Base
from sqlalchemy.orm import relationship

class DiaryInfo(Base):
    __tablename__ = "diary_info"

    id = Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True)
    diaryName = Column(String)
    diaryImage = Column(String)
    diaryDesc = Column(String)
    diaryShare = Column(Boolean, default=True)
    diaryOwnerId = Column(String, ForeignKey("user_info.id"))

    diaryOwner = relationship("UserInfo", back_populates="userDiaries")
    diaryPages = relationship("PageInfo", back_populates="pageDiary")