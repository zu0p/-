import mlxtend
# preprocessing에서 TransactionEncoder가져옴
from mlxtend.preprocessing import TransactionEncoder
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from mlxtend.frequent_patterns import fpgrowth
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from result_data import emotion_filter

app2 = FastAPI()

origins = ["*"]
app2.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Emotion(BaseModel):
    userId: str
    emotion: str


@app2.post('/music_reco')
def recommend_music(Emot: Emotion):
    userId = Emot.userId  # 추천 받을 사용자
    emotion = Emot.emotion  # 추천 시 필터할 감정
    # emotion = '긍정'
    data1 = np.array(emotion_filter(userId, emotion))
    data = np.array([
        ['serverpath/music1', 'serverpath/music2', 'serverpath/music3'],
        ['serverpath/music5', 'serverpath/music2', 'serverpath/music4'],
        ['serverpath/music1', 'serverpath/music5',
            'serverpath/music2', 'serverpath/music4'],
        ['serverpath/music5', 'serverpath/music4']
    ])
    print(data1)
    print(data)
    te = TransactionEncoder()  # 트랜잭션인코더 함수 호출 -> te로 저장
    # fit + transform 하면 array로 row+col
    te_ary = te.fit(data).transform(data)
    # te.columns_ : 트랜잭션인코더 해서 트랜잭션 매트릭스로 변경할때
    df = pd.DataFrame(te_ary, columns=te.columns_)
    #   컬럼 순서를 어떻게 기록하고있는지 정보를 가지고 있음
    # pd.DataFrame : array형태를 pands의 dataframe로 변경해줌

    # print(df)

    # 최소 지지도를 넘지 못한 item은 제외된다
    map = fpgrowth(df, min_support=0.01, use_colnames=True)
    map = map.sort_values(by='support',  # support 기준
                          ascending=False,  # 내림차순 정렬
                          axis=0
                          )
    # print(map)
    return "하이"
