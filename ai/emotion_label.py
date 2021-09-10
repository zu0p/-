

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import kss
import openpyxl
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
# import nltk
# nltk.download('punkt')
from konlpy.tag import Okt


# 엑셀 파일로 저장하기 위한 작업
excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.append(["content", "emotion"])


class List(list):
    def __str__(self):
        return "[" + ", ".join(["%s" % x for x in self]) + "]"


def test3():
    sentence = "대부분 온라인 강의이지만 한달에 한 두번은 꼭 장거리로 강의여행을 떠날 일이 생긴다."
    okt = Okt()
    word_list = (List(okt.morphs(sentence)))
    print(word_list[0])


def changeSentence():
    # write_data = pd.read_excel('article.xlsx')
    write_data = pd.read_excel('article2.xlsx', engine='openpyxl')
    # print(chatbot_data)
    print(write_data.columns)
    okt = Okt()
    df1 = write_data['content']  # title 버리고 content만 취함

    for i in range(len(df1)):
        temp = df1.loc[i]
        for sent in kss.split_sentences(temp):

            word_list = (List(okt.morphs(sent)))

            print(word_list[1])

            # excel_sheet.append([sent, ""])

    # excel_file.save("sentence_emotion2.xlsx")
    # excel_file.close


def main():
    # changeSentence()
    # test2()
    changeSentence()


if __name__ == '__main__':
    main()
