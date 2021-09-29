import mlxtend
# preprocessing에서 TransactionEncoder가져옴
from mlxtend.preprocessing import TransactionEncoder
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from mlxtend.frequent_patterns import fpgrowth
app = FastAPI()


@app.get('/music_reco')
def recommend_music():
    data = np.array([
        ['우유', '기저귀', '쥬스'],
        ['양상추', '기저귀', '맥주'],
        ['우유', '양상추', '기저귀', '맥주'],
        ['양상추', '맥주']
    ])

    te = TransactionEncoder()  # 트랜잭션인코더 함수 호출 -> te로 저장
    te_ary = te.fit(data).transform(data)  # fit + transform 하면 array로 row+col
    # te.columns_ : 트랜잭션인코더 해서 트랜잭션 매트릭스로 변경할때
    df = pd.DataFrame(te_ary, columns=te.columns_)
    #   컬럼 순서를 어떻게 기록하고있는지 정보를 가지고 있음
    # pd.DataFrame : array형태를 pands의 dataframe로 변경해줌

    print(fpgrowth(df, min_support=0.5, use_colnames=True)) #최소 지지도를 넘지 못한 item은 제외된다
    print(df)
    return "하이"
