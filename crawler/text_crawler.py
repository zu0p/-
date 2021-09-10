import pandas as pd
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import openpyxl
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

# 엑셀 파일로 저장하기 위한 작업
excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.append(["제목", "내용"])

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    chrome_options=options,  executable_path=r'C:\SSAFY\semester2\특화PJT\sub2\crawler\chromedriver.exe')


def infinite_scroll():
    elem = driver.find_element_by_tag_name("body")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        scroll_down = 0

        while scroll_down < 10:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)
            scroll_down += 1

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height


def next_article(link):
    driver.get(link)
    time.sleep(0.5)

    # 최근 열린 탭으로 전환
    # driver.switch_to_window(driver.window_handles[-1])

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1', {"class": "cover_title"}).text
    contents = soup.find_all(class_='item_type_text')
    content = ""
    for i in contents:
        str = i.text
        if str != '':
            content += str

    # openpyxl.utils.exceptions.IllegalCharacterError 해결
    title = ILLEGAL_CHARACTERS_RE.sub(r'', title)
    content = ILLEGAL_CHARACTERS_RE.sub(r'', content)
    excel_sheet.append([title, content])

    # 탭 종류 후 이전 탭으로 전환
    # driver.switch_to_window(driver.window_handles[0])


def main():

    # 페이지 로드를 위해 3초 대기
    driver.implicitly_wait(3)
    driver.get(
        'https://brunch.co.kr/keyword/%EA%B0%90%EC%84%B1_%EC%97%90%EC%84%B8%EC%9D%B4?q=g')

    infinite_scroll()

    # article 링크들 가져오기
    elems = driver.find_elements_by_css_selector('.list_has_image [href]')
    links = [elem.get_attribute('href') for elem in elems]

    for link in links:
        next_article(link)

    # 엑셀 파일로 저장
    excel_file.save("article.xlsx")
    excel_file.close()
    driver.quit()


if __name__ == '__main__':
    main()
