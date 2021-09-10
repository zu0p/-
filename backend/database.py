# https://fastapi.tiangolo.com/tutorial/sql-databases/
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

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

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # 상속 클래스를 자동으로 인지하고, 알아서 매핑해준다

def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()