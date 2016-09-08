# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from urllib.request import webdriver
from bs4 import BeautifulSoup

#하나는 자바스크립트 렌더링 전에 데이터를 받아 오는 것
def Spider():

  url = "https://play.google.com/store/apps/details?id=com.chbreeze.jikbang4a"
  source_code = requests.get(url) #타겟 url의 데이터를 파이썬으로 처리하기 위해 데이터를 불러오려고 하는데, 이 때 아래와 같이 requests.get(url)으로 데이터를 가져옵니다.
  plain_text = source_code.text
  soup = BeautifulSoup(plain_text, 'lxml')

  conn = urlopen(url)
  data = conn.read()
  conn.close()

  file = open('zigbang.xlsx', 'wt')
  file.write(data)
  file.close()

  browser = webdriver.chrome()
  broser.get('file:///'+'zigbang.xlsx')
  browser.quit()


  reviews = soup.select('.single-review')
  review_list = []
  review_filter = soup.select('.details-section.reviews > .details-section-contents >.review-filters')
  print(review_filter)

  for review in soup.select('.single-review'):
      review_list.append(review)
  # print(len(review_list))

  for review in review_list:
      review_date = str(review.select('.review-header > .review-info > .review-date')[0].text)
      if review_date == '2016년 9월 3일':
          review_text = review.select('.review-body')
          review_text = review_text[0].text
          print(review_date, review_text)


Spider()
