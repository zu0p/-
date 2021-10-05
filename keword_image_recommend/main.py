from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel
import database
import googletrans
from googletrans import Translator
app = FastAPI()


class Item(BaseModel):
    kewords: str


@app.get("/reco_image/")
def recommend_images(keyword: str):

    translator = Translator()
    trans3 = translator.translate(keyword, src='ko', dest='en')
    print("Korean to English: ", trans3.text)
    result_keyword = trans3.text
    reco_list = database.reco_image(result_keyword)
    print(len(reco_list))

    if len(reco_list) == 0:
        print("어떤 처리 필요하면 추후에 하기")
    return reco_list
