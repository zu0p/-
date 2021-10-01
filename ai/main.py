
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI
import numpy as np
import kss
import json
from konlpy.tag import Okt
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

app = FastAPI()
model = load_model('mlptkey/emotion_1.h5')
okt = Okt()
max_words = 35000
max_len = 20  # 전체 데이터의 길이를 20로 맞춘다
stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘',
             '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다', 'writing', "='", '.']

tokenizer = Tokenizer(num_words=max_words)

with open('mlptkey/wordIndex.json') as json_file:
    word_index = json.load(json_file)
    tokenizer.word_index = word_index


class Item(BaseModel):
    writing: str  # 입력으로 들어오는 글


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/emotion')
def emotion_extraction(item: Item):

    X2_test = []
    test_data = []
    item = str(item)

    for sent in kss.split_sentences(item):  # 글에서 문장 하나씩 가져오기
        test_data.append(sent)

    for sentence in test_data:
        temp_X2 = []
        temp_X2 = okt.morphs(sentence, stem=True)  # 토큰화
        temp_X2 = [word for word in temp_X2 if not word in stopwords]  # 불용어 제거
        X2_test.append(temp_X2)
        print(temp_X2)

    X2_test = tokenizer.texts_to_sequences(X2_test)
    X2_test = pad_sequences(X2_test, maxlen=max_len)

    print(X2_test)
    predict2 = model.predict(X2_test)
    predict2_labels = np.argmax(predict2, axis=1)
    print(predict2_labels[0], predict2_labels[1])
    check = [0, 0, 0]  # 중립,긍정,부정
    result = -1

    for i in range(len(predict2_labels)):
        check[predict2_labels[i]] = check[predict2_labels[i]] + 1

    if check[1] == check[2]:  # 긍정과 부정의 수가 같다면 중립(0)으로 도출하기
        result = 0
    else:
        result = max(check[1], check[2])

    return result
