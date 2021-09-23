
from sqlalchemy import Column,Integer,String
from sqlalchemy.dialects.mysql import INTEGER

from database import Base
from sqlalchemy.orm import relationship

class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True)
    userId = Column(String)
    userPwd = Column(String)
    userName = Column(String)
    userEmail = Column(String)
    userNick = Column(String)
    userPhone = Column(String)
    userImage = Column(String)
    
    userDiaries = relationship("DiaryInfo", back_populates="diaryOwner")
    # https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html