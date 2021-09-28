from sqlalchemy import Column,String,Boolean
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.mysql.types import TEXT
from sqlalchemy.sql.schema import ForeignKey

from database import Base
from sqlalchemy.orm import relationship

class PageInfo(Base):
    __tablename__ = "page_info"

    id = Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True)
    pageTitle = Column(String)
    pageContent = Column(TEXT)
    pageShare = Column(Boolean, default=True)
    pageDiaryId = Column(String)
    pageOwnerId = Column(String)
    pageImage = Column(String)
    top = Column(String)
    left = Column(String)

    pageDiary = relationship("DiaryInfo", back_populates="diaryPages")