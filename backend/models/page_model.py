from sqlalchemy import Column,String,Boolean
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.mysql.types import TEXT
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float

from database import Base
from sqlalchemy.orm import relationship

class PageInfo(Base):
    __tablename__ = "page_info"

    id = Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True)
    diaryId = Column(String, ForeignKey("diary_info.id"))
    pageTitle = Column(String)
    pageContent = Column(TEXT)
    pageShare = Column(Boolean, default=True)
    pageOwnerId = Column(String, ForeignKey("user_info.id"))
    pageImage = Column(String)
    top = Column(Float)
    left = Column(Float)

    pageDiary = relationship("DiaryInfo", back_populates="diaryPages")