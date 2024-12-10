# api 호출을 하기위해서는 web에서 요청이 가능한 라이브러리를 사용해야 함
# http 클라이언트라고 함 .. requests

import requests

res = requests.get('https://api.github.com/users/soongon')
print(res.text)

