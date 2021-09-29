# https://fastapi.tiangolo.com/tutorial/sql-databases/
import os
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.dialects.mysql.types import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import sqlalchemy

# ============================================ meta-data ============================================

metadata = sqlalchemy.MetaData()

user_info = sqlalchemy.Table(
    "user_info",
    metadata,
    sqlalchemy.Column("id", INTEGER(unsigned=True), autoincrement=True, primary_key=True),
    sqlalchemy.Column("userId", sqlalchemy.String(256)),
    sqlalchemy.Column("userPwd", sqlalchemy.String(256)),
    sqlalchemy.Column("userName", sqlalchemy.String(256)),
    sqlalchemy.Column("userEmail", sqlalchemy.String(256)),
    sqlalchemy.Column("userNick", sqlalchemy.String(256)),
    sqlalchemy.Column("userPhone", sqlalchemy.String(256)),
    sqlalchemy.Column("userImage", sqlalchemy.String(256))
)

diary_info = sqlalchemy.Table(
    "diary_info",
    metadata,
    sqlalchemy.Column("id", INTEGER(unsigned=True), autoincrement=True, primary_key=True),
    sqlalchemy.Column("diaryName", sqlalchemy.String(256)),
    sqlalchemy.Column("diaryImage", sqlalchemy.String(256)),
    sqlalchemy.Column("diaryDesc", sqlalchemy.String(256)),
    sqlalchemy.Column("diaryShare", sqlalchemy.Boolean(256)),
    sqlalchemy.Column("diaryOwnerId", sqlalchemy.String(256))
)

page_info = sqlalchemy.Table(
    "page_info",
    metadata,
    sqlalchemy.Column("id", INTEGER(unsigned=True), autoincrement=True, primary_key=True),
    sqlalchemy.Column("diaryId", sqlalchemy.INTEGER),
    sqlalchemy.Column("pageTitle", sqlalchemy.String(256)),
    sqlalchemy.Column("pageContent", sqlalchemy.TEXT),
    sqlalchemy.Column("pageShare", sqlalchemy.Boolean(256)),
    sqlalchemy.Column("pageOwnerId", sqlalchemy.String(256)),
    sqlalchemy.Column("pageImage", sqlalchemy.String(256)),
    sqlalchemy.Column("top", sqlalchemy.FLOAT),
    sqlalchemy.Column("left", sqlalchemy.FLOAT),
)
# ============================================ db-info ============================================

# local
# db_user = "root"
# db_password = "root"
# db_name = "ssafy_fastapi_web"
# db_server = "localhost:3306"

# aws
db_user = "test"
db_password = "test"
db_name = "ssafy_fastapi_web"
db_server = "j5d103.p.ssafy.io:3306"

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_server}/{db_name}"
#SQLALCHEMY_DATABASE_URL = os.environ['SQLALCHEMY_DB_URL']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping= True, # 소극적 disconnect_handling
)
metadata.create_all(engine)

# ============================================ db-usage ============================================

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # 상속 클래스를 자동으로 인지하고, 알아서 매핑해준다

def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()