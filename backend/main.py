from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from views.user_views import user_router

server = FastAPI(title='APIs for 그리더(당신의 글에 이미지를 더하다) 젠킨스 배포 완료!!!!', description='그리더(당신의 글에 이미지를 더하다)', version='0.1')
server.mount("/static", StaticFiles(directory="static"), name="static")

# prefix 지정
server.router.prefix = "/api/v1"

# router 설정
server.include_router(user_router, prefix="/users")
