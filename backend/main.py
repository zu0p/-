from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from starlette.staticfiles import StaticFiles

from views.user_views import user_router
from views.diary_views import diary_router
from views.page_views import page_router

tags_metadata = [
    {
        "name": "회원관리",
        "description": "회원관리 API",
    },
    {
        "name": "다이어리",
        "description": "다이어리 API",
    },
    {
        "name": "일기관리",
        "description": "일기관리 API",
    },
    {
        "name": "추천관리",
        "description": "추천관리 API",
    },
    # {
    #     "name": "items",
    #     "description": "Manage items. So _fancy_ they have their own docs.",
    #     "externalDocs": {
    #         "description": "Items external docs",
    #         "url": "https://fastapi.tiangolo.com/",
    #     },
    # },
]

server = FastAPI(
                title='APIs for 그리더(당신의 글에 이미지를 더하다)', 
                description=' Greeder Backend System, Made by FastAPI', 
                version='0.1', 
                # terms_of_service="http://example.com/terms/",
                contact={
                        "name": "Seungyeup Lee",
                        "url": "https://buildabetterworld.tistory.com/",
                        "email": "lsyeup1206@naver.com",
                    },
                license_info={
                    "name": "Apache 2.0",
                    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                },
                openapi_tags=tags_metadata
            )

server.mount("/static", StaticFiles(directory="static"), name="static")

# CORS 설정
origins = [
    "*"
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# prefix 지정
server.router.prefix = "/api/v1"

# router 설정
server.include_router(user_router, prefix="/users", tags=["회원관리"])
server.include_router(diary_router, prefix="/diary", tags=["다이어리"])
server.include_router(page_router, prefix="/page", tags=["일기관리"])
server.include_router(recommend_router, prefix="/recommend", tags=["추천관리"])
