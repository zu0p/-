import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import googletrans
import pymysql

db = None


def image_crawling(keyword):
    driver = driver_init()
    # 한글 -> 영어 번역
    keyword = googletrans.Translator().translate(keyword, dest='en').text

    url = 'https://unsplash.com/s/photos/' + keyword
    # 페이지 로드를 위해 3초 대기
    driver.implicitly_wait(3)
    driver.get(url)

    elem = driver.find_element_by_tag_name("body")
    for i in range(5):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.4)

    images = driver.find_elements_by_class_name("oCCRx")
    n = 1
    img_descs = []
    img_save_urls = []
    for image in images:
        img_urls = image.get_attribute('srcset')
        img_desc = image.get_attribute('alt')

        if img_urls is None:
            continue

        img_urls = img_urls.split()

        if len(img_urls) < 1:
            continue

        img_url = img_urls[20]
        img_descs.append(img_desc)

        with urlopen(img_url) as f:
            with open('../images/keywords/' + keyword + str(n) + '.jpg', 'wb') as h:  # 이미지 + 사진번호 .jpg
                img = f.read()  # 이미지 읽기
                h.write(img)
        img_save_urls.append(
            '/home/ubuntu/images/keywords/' + keyword + str(n) + '.jpg')
        n += 1
        if n > 20:
            break

    driver.close()
    return keyword, img_save_urls, img_descs


def driver_init():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        chrome_options=options,  executable_path=r'../chromedriver')

    return driver


def main():
    global db

    db = pymysql.connect(
        user='test',
        passwd='test',
        host='13.124.43.16',
        db='ssafy_django_web',
        charset='utf8'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)

    df = pd.read_excel(
        './keywords(초기850개).xlsx', engine='openpyxl')
    keywords = df['키워드']

    cnt = 0
    for word in keywords:
        cnt += 1

        if (cnt > 5):
            break

        key, img_urls, img_descs = image_crawling(word)
        for i in range(len(img_urls)):
            sql = "INSERT INTO `image` VALUES (%s, %s, %s, %s);"
            val = (0, key, img_descs[i], img_urls[i])
            # val = [['id', 0], ['keyword', key], [
            #     'desc', img_descs[i]], ['url', img_urls[i]]]

            cursor.execute(sql, val)

            db.commit()


if __name__ == '__main__':
    main()
