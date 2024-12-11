import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

products = []
for product in soup.select('#productList > li'):
    products.append([
        product.select_one('a > dl > dd > div.name').text.strip(),
        product.select_one('a > dl > dd > div.price-area > div > div.price > em > strong').text,
        product.select_one('a > dl > dd > div.other-info > div > span.star > em').text,
        product.select_one('a > dl > dt > img')['src'],
    ])

print(products)


