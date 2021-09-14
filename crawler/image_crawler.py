import pandas as pd
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import openpyxl
import requests
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from urllib.parse import quote_plus


def main():
    keyword = 'dad'
    url = 'https://unsplash.com/s/photos/' + keyword
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all(class_='oCCRx', limit=30)  # 클래스가 oCCRx인 사진 20장
    print(images)

    n = 1
    for image in images:
        img_urls = image['srcset'].split()
        img_url = img_urls[20]
        print(img_url)
        with urlopen(img_url) as f:
            with open('./img/' + keyword + str(n) + '.jpg', 'wb') as h:  # 이미지 + 사진번호 .jpg
                img = f.read()  # 이미지 읽기
                h.write(img)
        n += 1


if __name__ == '__main__':
    main()
