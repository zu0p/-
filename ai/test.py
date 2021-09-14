import pandas as pd


def main():
    emotion_dir = pd.read_excel('emotion_directory.xlsx', engine='openpyxl')
    emotion_dir = emotion_dir.fillna(0)
    # print(chatbot_data)
    # print(write_data.columns)
    dir1 = emotion_dir[['단어', '감정범주']]

    list = dir1.values.tolist()
    temps = ["재미", "있는", "사실", "가서도", "온라인", "스튜디오", "에서", "온라인", "으로", "수업", "한다는", "이다"]
    stop_list = ["이다","있다","있어","해서","해도","했지만","하다","한다","했다"]
    result = []
    for w in temps:
        if w not in stop_list:
            result.append(w)
    for i in range(len(list)):
        if list[i][0] == 0:
            break
        for j in range(len(result)):
            if list[i][0].find(result[j]) !=-1:
               print(list[i][0])


if __name__ == '__main__':
    main()
