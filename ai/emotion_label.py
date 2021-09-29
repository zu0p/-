

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
word_list = []


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
    write_data = pd.read_excel('article.xlsx', engine='openpyxl')
    write_data = write_data.where(pd.notnull(write_data), None)
    emotion_dir = pd.read_excel('emotion_directory.xlsx', engine='openpyxl')
    emotion_dir = emotion_dir.fillna(0)

    # print(chatbot_data)
    # print(write_data.columns)
    okt = Okt()
    df1 = write_data['content']  # title 버리고 content만 취함
    dir1 = emotion_dir[['단어', '감정범주']]
    list_dir1 = dir1.values.tolist()
    # check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    check = []
    cnt = 0
    emotion = ['혐오', '기쁨', '슬픔', '중립', '기타', '분노', '흥미', '지루함', '놀람', '통증']
    for i in range(len(df1)):
        if(df1.loc[i] is None):  # 공백시 보지 않음
            continue
        cnt = cnt+1
        print(cnt)
        stop_list = ["이다", "있다", "있어", "해서", "해도", "했지만", "하다", "한다", "했다"]
        # print(len(df1))
        temp = str(df1.loc[i])  # 글 하나씩 가져오기
        for sent in kss.split_sentences(temp):  # 글에서 문장 하나씩 가져오기
            word_list = []
            check = []
            check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            word_lists = (List(okt.morphs(sent)))  # 문장에서 키워드 단어들 가져오기
            for w in word_lists:  # 직접 정의한 불용어 처리
                if w not in stop_list:
                    word_list.append(w)

            for j in range(len(word_list)):  # 단어가 감정사전에 포함되 있는 단언지 확인하기
                if type(word_list[j]) == type("test"):  # 숫자 들어올 때 거름
                    if len(word_list[j]) <= 1:  # 1글자 짜리로 감정 예측하지 않기
                        continue
                    for u in range(len(list_dir1)):
                        if(list_dir1[u][1] == 0):
                            break
                        if list_dir1[u][0].find(word_list[j]) != -1:
                            if list_dir1[u][1] == '혐오':
                                check[0] = int(check[0])+1
                                break

                            elif list_dir1[u][1] == '기쁨':
                                check[1] = int(check[1])+1
                                break

                            elif list_dir1[u][1] == '슬픔':
                                check[2] = int(check[2])+1
                                break

                            elif list_dir1[u][1] == '중성':
                                check[3] = check[3]+1
                                break

                            elif list_dir1[u][1] == '기타':
                                check[4] = int(check[4])+1
                                break

                            elif list_dir1[u][1] == '분노':
                                check[5] = int(check[5])+1
                                break

                            elif list_dir1[u][1] == '흥미':
                                check[6] = int(check[6])+1
                                break

                            elif list_dir1[u][1] == '지루함':
                                check[7] = check[7]+1
                                break

                            elif list_dir1[u][1] == '놀람':
                                check[8] = int(check[8])+1
                                break

                            elif list_dir1[u][1] == '통증':
                                check[9] = int(check[9])+1
                                break

            if max(check) == 0:
                excel_sheet.append([sent, "중립"])
            else:
                idx = check.index(max(check))
                if idx == 3 | idx == 4:
                    check[3] = 0
                    check[4] = 0
                    idx = check.index(max(check))
                    if max(check) == 0:
                        excel_sheet.append([sent, "중립"])
                    else:
                        excel_sheet.append([sent, check[idx]])
                else:
                    excel_sheet.append([sent, emotion[idx]])

            check = []
        excel_file.save("sentence_emotion2.xlsx")
        excel_file.close


def main():
    # changeSentence()
    # test2()
    changeSentence()


if __name__ == '__main__':
    main()
