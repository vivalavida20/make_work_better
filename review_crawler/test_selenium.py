# -*- coding: utf-8 -*-
import pandas
from pandas import Series, DataFrame
import xlsxwriter

import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver


#하나는 그냥 있는 유니크 리뷰 순을 excel데이터로 저장하는 것
def Spider():

  # url = "https://play.google.com/store/apps/details?id=com.chbreeze.jikbang4a"
  # source_code = requests.get(url) #타겟 url의 데이터를 파이썬으로 처리하기 위해 데이터를 불러오려고 하는데, 이 때 아래와 같이 requests.get(url)으로 데이터를 가져옵니다.
  # plain_text = source_code.text
  # soup = BeautifulSoup(plain_text, 'lxml')
  # reviews = soup.select('.single-review')
  review_list = []
  current_time = time.strftime('%x').replace('/', '')
  print(current_time)
  driver = webdriver.Firefox()
  driver.get('https://play.google.com/store/apps/details?id=com.chbreeze.jikbang4a')

  html = driver.page_source
  soup = BeautifulSoup(html)
  prodList = soup.find_all("div", {"class": "single-review"})


  for prod in prodList:
      review_list.append(prod)

  print(review_list)


Spider()
