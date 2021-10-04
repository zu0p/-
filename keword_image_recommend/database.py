import pymysql
import random


def reco_image(keyword):
    result_rows = []
    final_rows = []
    conn = pymysql.connect(host='j5d103.p.ssafy.io', user='test', password='test', db='ssafy_django_web',
                           charset='utf8')
    curs = conn.cursor()
    # sql = "select * from like_image where keword=%s order by like_count desc limit 2 "
    sql = "select * from like_image where keword=%s order by like_count desc"
    curs.execute(sql, (keyword))
    rows = curs.fetchall()
    conn.close()
    if len(rows) > 0:
        result_rows.append(rows[0])
        result_rows.append(rows[1])
        rnum1 = random.randint(2, len(rows))
        rnum2 = rnum1

        while rnum1 == rnum2:
            rnum2 = random.randint(2, len(rows))
        result_rows.append(rows[rnum1])
        result_rows.append(rows[rnum2])

    for i in range(len(result_rows)):
        final_rows.append({
            "id": result_rows[i][0],
            "keyword": result_rows[i][1],
            "count": result_rows[i][2],
            "url": result_rows[i][3]
        })

    return final_rows
