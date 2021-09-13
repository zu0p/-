import pandas as pd
from konlpy.tag import Kkma
from konlpy.tag import Twitter
from konlpy.tag import Okt
from nltk.tokenize.punkt import PunktSentenceTokenizer
from scipy.sparse.sputils import matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import openpyxl
import numpy as np
import time

kkma = Kkma()
okt = Okt()


def main():
    start = time.time()
    df = pd.read_excel(
        'C:/SSAFY/semester2/특화PJT/ai/article.xlsx', engine='openpyxl')
    df_stopwords = pd.read_excel(
        'C:/SSAFY/semester2/특화PJT/ai/stop_words.xlsx', engine='openpyxl')

    stopwords = df_stopwords['형태'].tolist()
    contents = df['내용']

    dic = {}

    for idx in range(len(contents)):
        sentences = get_sentences(contents[idx])
        nouns = get_nouns(sentences, stopwords)
        keywords = get_keywords(nouns, 5)

        for keyword in keywords:
            if keyword in dic:
                dic[keyword] = dic.get(keyword) + 1
            else:
                dic[keyword] = 1

    sorted_dic = sorted(dic.items(), reverse=True, key=lambda item: item[1])
    # 엑셀 파일로 저장
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.active
    excel_sheet.append(["키워드", "빈도수"])

    for row in sorted_dic:
        excel_sheet.append(row)

    excel_file.save("keywords.xlsx")
    excel_file.close()
    print("수행 시간(초) : ", time.time() - start)


def tf_idf(sentences):
    # 문장을 넣으면 문장 단위로 tf-idf 수치를 벡터화
    vectorizer = TfidfVectorizer()
    tfidf_mat = vectorizer.fit_transform(sentences).toarray()

    graph_sentence = np.dot(tfidf_mat, tfidf_mat.T)

    # 정수 인덱스 이름 불러오기
    # print(vectorizer.get_feature_names())

    return graph_sentence


def cv(sentences):
    # 텍스트를 토큰 매트릭스로 변환
    cv = CountVectorizer()
    cv_mat = normalize(cv.fit_transform(
        sentences).toarray().astype(float), axis=0)

    vocab = cv.vocabulary_
    idx_to_word = {vocab[word]: word for word in vocab}
    graph_word = np.dot(cv_mat, cv_mat.T)

    return idx_to_word, graph_word


def get_keywords(nouns, num):
    idx_to_word, graph_word = cv(nouns)
    ranks = get_ranks(graph_word)
    sort_ranks = sorted(ranks, key=lambda k: ranks[k], reverse=True)

    keywords = []
    index = []
    for idx in sort_ranks[:num]:
        index.append(idx)

    for idx in index:
        keywords.append(idx_to_word[idx])

    return keywords


def get_ranks(graph, d=0.85):  # d = damping factor
    A = graph
    matrix_size = A.shape[0]
    for id in range(matrix_size):
        A[id, id] = 0
        col_sum = np.sum(A[:, id])  # A[:, id] = A[:][id]
        if col_sum != 0:
            A[:, id] /= col_sum
        A[:, id] *= -d
        A[id, id] = 1

    B = (1-d) * np.ones((matrix_size, 1))

    ranks = np.linalg.solve(A, B)  # 연립방적식 Ax = b
    return {idx: r[0] for idx, r in enumerate(ranks)}


def get_sentences(text):
    sentences = kkma.sentences(text)
    return sentences


def get_nouns(sentences, stopwords):
    nouns = []

    for sentence in sentences:
        if sentence is not '':
            noun = [noun for noun in okt.nouns(str(sentence))
                    if noun not in stopwords and len(noun) > 1]
            if len(noun) > 0:
                nouns.append(' '.join(noun))
    return nouns


if __name__ == '__main__':
    main()
