# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def Spider():

  url = "https://play.google.com/store/apps/details?id=com.chbreeze.jikbang4a"
  source_code = requests.get(url) #타겟 url의 데이터를 파이썬으로 처리하기 위해 데이터를 불러오려고 하는데, 이 때 아래와 같이 requests.get(url)으로 데이터를 가져옵니다.
  plain_text = source_code.text
  soup = BeautifulSoup(plain_text, 'lxml')
  reviews = soup.select('.single-review')
  review_list = []
  review_filter = soup.select('.details-section.reviews > .details-section-contents >.review-filters')
  print(review_filter)

  for review in soup.select('.single-review'):
      review_list.append(review)
  print(len(review_list))

  for review in review_list:
      review_date = str(review.select('.review-header > .review-info > .review-date')[0].text)
      if review_date == '2016년 9월 3일':
          review_text = review.select('.review-body')
          review_text = review_text[0].text
          print(review_date, review_text)


Spider()
