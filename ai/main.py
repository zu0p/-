import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
import kss
from tqdm import tqdm, tqdm_notebook
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model
from transformers import AdamW
from transformers.optimization import get_cosine_schedule_with_warmup
# from bert_model import BERTClassifier
# from bertDataSet import BERTDataset
from emotion_extraction import bert_model
from emotion_extraction import bertDataSet

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


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
    max_len = 64
    batch_size = 64
    warmup_ratio = 0.1
    num_epochs = 20
    max_grad_norm = 1
    log_interval = 200
    learning_rate = 5e-5
    device = torch.device('cpu')
    bertmodel, vocab = get_pytorch_kobert_model()
    # 토큰화
    tokenizer = get_tokenizer()
    tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

    model = bert_model.BERTClassifier(bertmodel,  dr_rate=0.5).to(device)
    # Prepare optimizer and schedule (linear warmup and decay)
    no_decay = ['bias', 'LayerNorm.weight']
    optimizer_grouped_parameters = [
        {'params': [p for n, p in model.named_parameters() if not any(
            nd in n for nd in no_decay)], 'weight_decay': 0.01},
        {'params': [p for n, p in model.named_parameters() if any(
            nd in n for nd in no_decay)], 'weight_decay': 0.0}
    ]

    optimizer = AdamW(optimizer_grouped_parameters, lr=learning_rate)
    loss_fn = nn.CrossEntropyLoss()
    # 전체 모델을 통째로 불러옴, 클래스 선언 필수
    # model = torch.load('../../model/3emotions_model2.pt', map_location=device)
    # state_dict를 불러 온 후, 모델에 저장
    model.load_state_dict(torch.load(
        'mlptkey/3emotions_model_state_dict2.pt', map_location=device))

    checkpoint = torch.load('mlptkey/3emotions_all2.tar',
                            map_location=device)   # dict 불러오기
    model.load_state_dict(checkpoint['model'])
    optimizer.load_state_dict(checkpoint['optimizer'])

    # dataset_another = [['영화에 나오는 귀신이 너무 무섭네요', '0'], ['그게 사실이야? 대박', '0'], ['배고파서 화가 난다', '0'],
    #                    ['그런 일이 있었다니 참 안타깝다', '0'], ['오늘은 비가 온다고 해요~', '0'], ['대학교에 붙어서 기분이 너무 좋다', '0'], ['수준 너무 떨어진다~', '0']]

    total = []
    item = str(item)
    for sent in kss.split_sentences(item):  # 글에서 문장 하나씩 가져오기
        sentence = []
        sentence.append(sent)
        sentence.append('0')
        total.append(sentence)

    another_test = bertDataSet.BERTDataset(
        total, 0, 1, tok, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(
        another_test, batch_size=batch_size, num_workers=5)

    model.eval()
    result = -1
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(tqdm_notebook(test_dataloader)):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length = valid_length
        label = label.long().to(device)
        out = model(token_ids, valid_length, segment_ids)

        test_eval = []
        for i in out:
            logits = i
            logits = logits.detach().cpu().numpy()
            test_eval.append(np.argmax(logits))  # 문장 감정 도출 값

        print(test_eval)  # 모든 문장에 대한 감정값 들어가 있음.
        result = int(max(test_eval, key=test_eval.count))  # 가장 많은 감정 값 저장

        check = [0, 0, 0]  # 중립,긍정,부정

        for i in range(len(test_eval)):
            check[test_eval[i]] = check[test_eval[i]] + 1

        if result == 0:  # 중립이 가장 많을 때는 긍정과 부정 중 가장 큰 값으로 도출하기
            result = max(check[1], check[2])
        if check[1] == check[2]:  # 긍정과 부정의 수가 같다면 중립(0)으로 도출하기
            result = 0

    return result
