from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel
import database
import googletrans
from googletrans import Translator
app = FastAPI()


class Item(BaseModel):
    kewords: str


translator = Translator()


@app.get("/image/{keyword}")  # 키워드가 디비에 있는지 여부확인
def check_keyword(keyword: str):
    trans = translator.translate(keyword, src='ko', dest='en')
    print("Korean to English: ", trans.text)
    result_keyword = trans.text

    reco_list = database.reco_image(result_keyword)
    if len(reco_list) == 0:
        return "false"
    else:
        return "true"


@app.get("/image/recommend/{keyword}")  # 상위 3개 + 랜덤 1개
def recommend_image(keyword: str):

    # translator = Translator()
    trans3 = translator.translate(keyword, src='ko', dest='en')
    print("Korean to English: ", trans3.text)
    result_keyword = trans3.text
    reco_list = database.reco_image(result_keyword)
    print(len(reco_list))

    if len(reco_list) == 0:
        print("어떤 처리 필요하면 추후에 하기")
    return reco_list


@app.get("/image/select/{url}")  # 사진 선택 시 선택 개수 증가
def plus_image(url: str):
    database.plus_image(url)
    return "true"
