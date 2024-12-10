client_id = 'b9goKJRqP8YsJ_9RJ1jn'
client_secret = 'yXKX2L4VKG'

import requests
import pandas as pd

params = {
    'query': '이효리'
}
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}
# 데이터 수집..
res = requests.get('https://openapi.naver.com/v1/search/blog.json', params=params, headers=headers)
# 데이터 정리 .. 엑셀로 저장..
items = res.json().get('items')

df = pd.DataFrame(items)
# 엑셀로 저장..
df.to_excel('naver_search_result.xlsx')
print('job completed..')