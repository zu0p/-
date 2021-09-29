import pymysql


def emotion_filter(userId, emotion):  # 동일아이디 제외, 같은 감정의 음악파일들만 반환하기

    # Mysql Connection 연결
    conn = pymysql.connect(host='j5d103.p.ssafy.io', user='test',
                           password='test', db='ssafy_fastapi_web', charset='utf8')

    # Connection 으로부터 Dictoionary Cursor 생성
    # curs = conn.cursor(pymysql.cursors.DictCursor)
    curs = conn.cursor()
    sql = "select musicName from music_info where userId!=%s and emotion = %s"
    curs.execute(sql, (userId, emotion))

    rows = curs.fetchall()

    size = rows.index

    return rows
