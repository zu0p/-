import pymysql
import random


def plus_image(url):
    print(url)
    conn = pymysql.connect(host='j5d103.p.ssafy.io', user='test', password='test', db='ssafy_django_web',
                           charset='utf8')
    curs = conn.cursor()
    sql = "UPDATE image SET like_count=like_count +1 WHERE url = %s"
    # curs.execute(sql, (url))
    print(curs.execute(sql, url))
    conn.commit()
    conn.close()


def reco_image(keyword):
    result_rows = []
    final_rows = []
    conn = pymysql.connect(host='j5d103.p.ssafy.io', user='test', password='test', db='ssafy_django_web',
                           charset='utf8')
    curs = conn.cursor()
    # sql = "select * from like_image where keword=%s order by like_count desc limit 2 "
    sql = "select * from image where keyword=%s order by like_count desc"
    curs.execute(sql, (keyword))
    rows = curs.fetchall()
    conn.close()
    if len(rows) > 0:
        result_rows.append(rows[0])
        result_rows.append(rows[1])
        result_rows.append(rows[2])
        result_rows.append(rows[random.randint(3, len(rows))])

    for i in range(len(result_rows)):
        final_rows.append({
            "id": result_rows[i][0],
            "keyword": result_rows[i][1],
            "like_count": result_rows[i][2],
            "url": result_rows[i][3]
        })

    return final_rows
