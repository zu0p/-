import pandas as pd
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import googletrans


def image_crawling(keyword):
    driver = driver_init()
    # 한글 -> 영어 번역
    eng_keyword = googletrans.Translator().translate(keyword, dest='en').text

    url = 'https://unsplash.com/s/photos/' + eng_keyword
    # 페이지 로드를 위해 3초 대기
    driver.implicitly_wait(3)
    driver.get(url)

    elem = driver.find_element_by_tag_name("body")
    for i in range(5):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.4)

    images = driver.find_elements_by_class_name("oCCRx")
    n = 1
    img_list = []
    for image in images:
        img_urls = image.get_attribute('srcset')
        img_desc = image.get_attribute('alt')

        if img_urls is None:
            continue

        img_urls = img_urls.split()

        if len(img_urls) < 1:
            continue

        img_url = img_urls[20]
        temp = [img_desc]
        img_list.append(temp)
        with urlopen(img_url) as f:
            with open('./crawler/images/' + keyword + str(n) + '.jpg', 'wb') as h:  # 이미지 + 사진번호 .jpg
                img = f.read()  # 이미지 읽기
                h.write(img)
        n += 1
        if n > 5:
            break
    print(img_list)


def driver_init():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        chrome_options=options,  executable_path=r'C:/SSAFY/2학기/특화PJT/특화PJT/crawler/chromedriver.exe')

    return driver


def main():
    image_crawling("엄마")


if __name__ == '__main__':
    main()
