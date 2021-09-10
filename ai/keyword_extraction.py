import pandas as pd
from konlpy.tag import Kkma
from konlpy.tag import Twitter
from konlpy.tag import Okt
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np
import time

kkma = Kkma()
okt = Okt()


def main():
    df = pd.read_excel(
        'C:/SSAFY/semester2/특화PJT/ai/article.xlsx', engine='openpyxl')
    df_stopwords = pd.read_excel(
        'C:/SSAFY/semester2/특화PJT/ai/stop_words.xlsx', engine='openpyxl')

    stopwords = df_stopwords['형태'].tolist()
    contents = df['content']

    sentences = get_sentences(contents[0])
    nouns = get_nouns(sentences, stopwords)
    print(nouns)


def get_sentences(text):
    sentences = kkma.sentences(text)
    return sentences


def get_nouns(sentences, stopwords):
    nouns = []

    for sentence in sentences:
        if sentence is not '':
            nouns.append(' '.join([noun for noun in okt.nouns(str(sentence))
                                   if noun not in stopwords and len(noun) > 1]))
    return nouns


if __name__ == '__main__':
    main()
