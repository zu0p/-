import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm, tqdm_notebook
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model
from transformers import AdamW
from transformers.optimization import get_cosine_schedule_with_warmup
from bert_model import BERTClassifier
from bertDataSet import BERTDataset
# Setting parameters


def main():
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
    model = BERTClassifier(bertmodel,  dr_rate=0.5).to(device)
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
    model1 = torch.load('../../model/3emotions_model2.pt', map_location=device)
    # state_dict를 불러 온 후, 모델에 저장
    model1.load_state_dict(torch.load(
        '../../model/3emotions_model_state_dict2.pt', map_location=device))

    checkpoint = torch.load('../../model/3emotions_all2.tar',
                            map_location=device)   # dict 불러오기
    model1.load_state_dict(checkpoint['model'])
    optimizer.load_state_dict(checkpoint['optimizer'])

    print("gd")
    dataset_another = [['영화에 나오는 귀신이 너무 무섭네요', '2'], ['그게 사실이야? 대박', '1'], ['배고파서 화가 난다', '2'],
                       ['그런 일이 있었다니 참 안타깝다', '2'], ['오늘은 비가 온다고 해요~', '0'], ['대학교에 붙어서 기분이 너무 좋다', '1'], ['수준 너무 떨어진다~', '2']]

    predict(dataset_another, model1)

    # emotion_model = torch.load(
    #     '../../model/emotion_model.pkl', map_location=device)


def predict(dataset_another, model1):
    max_len = 64
    batch_size = 64
    warmup_ratio = 0.1
    num_epochs = 20
    max_grad_norm = 1
    log_interval = 200
    learning_rate = 5e-5
    device = torch.device('cpu')
    tokenizer = get_tokenizer()
    bertmodel, vocab = get_pytorch_kobert_model()
    tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)
    # 토큰화

    another_test = BERTDataset(
        dataset_another, 0, 1, tok, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(
        another_test, batch_size=batch_size, num_workers=5)

    model1.eval()

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(tqdm_notebook(test_dataloader)):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)

        valid_length = valid_length
        label = label.long().to(device)

        out = model1(token_ids, valid_length, segment_ids)

        test_eval = []
        for i in out:
            logits = i
            logits = logits.detach().cpu().numpy()
            test_eval.append(np.argmax(logits))

        print(test_eval)


if __name__ == '__main__':
    main()
