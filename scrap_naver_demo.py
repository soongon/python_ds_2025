import requests
from bs4 import BeautifulSoup

# html 확보
res = requests.get('https://finance.naver.com/')

# bs 사용해서 파싱가능하게 만든다.
soup = BeautifulSoup(res.text, 'html.parser')

# 원하는 데이터를 추출(파싱)하면 된다.
the_tag = soup.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num')
print(the_tag.text)
