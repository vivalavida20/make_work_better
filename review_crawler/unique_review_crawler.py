# -*- coding: utf-8 -*-
import pandas
from pandas import Series, DataFrame
from pandas import ExcelWriter
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

  #리스트형태로 만들기
  for prod in prodList:
      review_list.append(prod)


  # print(review_list)

  review_text_list = []
  review_date_list = []
  review_author_list = []
  review_rating_list = []
  for review in review_list:
      review_date = str(review.select('.review-header > .review-info > .review-date')[0].text)
      review_author = str(review.select('.review-header > .review-info > .author-name')[0].text)
      review_text = review.select('.review-body')
      review_text = review_text[0].text
      review_text = review_text.replace('전체 리뷰', '')

      review_date_list.append(review_date)
      review_author_list.append(review_author)
      review_text_list.append(review_text)

  review_data = {'date':review_date_list,
                 'author':review_author_list,
                 'text':review_text_list}
  review_data_frame = DataFrame(review_data)
  print(review_data_frame)

  #꺼내온 DataFrame을 excel파일에 저장하기
  #pandas에서 excel을 쓰려면 writer라는 객체를 생성해야 한단다. 왠지는 안알아봄.
  try:
      writer = ExcelWriter('dabang.xlsx')
      review_data_frame.to_excel(writer,'sheet%s' % current_time)
      writer.save()

      print('Successfully saved')
  except:
      print('Failed to Save')

  #excel에 저장은 했는데, 각 날짜별로 서로 다른 sheet에 저장하고픔

Spider()
