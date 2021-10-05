import os
import asyncio
import aiofiles
import logging
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, status, FastAPI, File, Form, UploadFile
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import requests 
import json
from database import get_db
import random
from schemas import user_schemas
from schemas import diary_schemas # schemas
from models import user_model, diary_model # models
from crud import user_crud, music_recommend ,diary_crud, page_crud # crud

import pandas as pd
from sklearn import preprocessing
from sklearn.metrics.pairwise import cosine_similarity


logger = logging.getLogger()
logger.setLevel(logging.INFO)

recommend_router = APIRouter()

# ================================== music recommendation CRUD ==================================

### 음악추천 랜덤 5
@recommend_router.get("/recommend_by_page/{diaryId}/{pageId}")
async def recommend_music_random_5( 
                        pageId: str,
                        diaryId: str,
                        db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):
    # 1. data load
    music_origin = music_recommend.return_musics_in_pdObject()
    read_one_page = music_recommend.return_pageInfo_in_pdObject(diaryId, pageId)
    
    # 2. sementic analysis request
    sementic_URL = 'http://13.125.248.60:8999/emotion'
    data = {
        "writing" : read_one_page.iloc[0]['pageContent'] 
    }
    res = requests.post(sementic_URL, data=json.dumps(data))
    # print(res.text)

    # 3. 유사 감정 음악 추출
    music_sementic = music_origin[music_origin['sementic']==int(res.text)]
    similar_music = music_sementic['id'].to_list()
    similar_music_random = random.sample(similar_music, 5)

    # 4. 반환형태로 변환해서 리턴
    Base_url = "https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/"
    result = []
    for s in similar_music_random:
        tmp = {}
        tmp["musicId"] = s
        genre = tmp["genre"] = music_origin.loc[s]["label"]
        musicName = tmp["musicName"] = music_origin.loc[s]["filename"]
        tmp["link"] = Base_url + f"music/{genre}/{musicName}"
        result.append(tmp)

    return result


### 유사 음악 TOP 5 추천s

def find_similar_songs(id, sim_df, n=5):
    series = sim_df[id].sort_values(by = id, ascending=False)
    series = series.drop(id).head(n)
    return series
    

# 유사도 분석, 코사인 유사도
@recommend_router.get("/recommend_by_content/{musicName}")
async def recommend_music_top_5( 
                        musicName: str,
                        db: Session = Depends(get_db),
                        current_user: user_schemas.UserInDB = Depends(user_crud.get_current_user)):

    # 1. data load
    music_origin = music_recommend.return_musics_in_pdObject()
    labels = music_origin[['label']]
    music_data = music_origin.drop(columns=['length','label','sementic','id','filename']) # 코사인 유사도 분석에 쓸모없는건 다뺀다.
    music_data_scaled = preprocessing.scale(music_data)
    music_data = pd.DataFrame(music_data_scaled, columns=music_data.columns)

    # 2. 유사도 설정
    similarity = cosine_similarity(music_data)
    sim_df = pd.DataFrame(similarity, index=labels.index, columns=labels.index)

    # 3. 유사 음악 추출
    id = music_origin.index[music_origin['filename'] == musicName].tolist()
    res = find_similar_songs(id, sim_df)
    
    # 4. 반환형태로 변환해서 리턴
    Base_url = "https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/"
    result = []
    for r in res.index.to_list():
        tmp = {}
        tmp["musicId"] = r
        genre = tmp["genre"] = music_origin.loc[r]["label"]
        musicName = tmp["musicName"] = music_origin.loc[r]["filename"]
        tmp["link"] = Base_url + f"music/{genre}/{musicName}"
        result.append(tmp)

    return result


