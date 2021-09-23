# from models.user_model import UserInfo

from sqlalchemy import Column,String,Boolean
from sqlalchemy.dialects.mysql import INTEGER

from database import Base
from sqlalchemy.orm import relationship

class DiaryInfo(Base):
    __tablename__ = "diary_info"

    id = Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True)
    diaryOwner = relationship("UserInfo", back_populates="userDiaries")
    diaryName = Column(String)
    diaryImage = Column(String)
    diaryDesc = Column(String)
    diaryShare = Column(Boolean, default=True)