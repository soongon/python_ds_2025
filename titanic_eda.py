# 데이터분석..
# 데이터를 로딩.. 데이터를 메모리에 로딩해서 분석 할 준비..
# 사용하는 라이브러리 .. pandas
# 판다스 설치 .. pip install pandas
import pandas as pd

# csv 파일 읽기
df = pd.read_csv('train.csv')

# 파일의 사이즈 확인
print(df.shape)

# 변수를 확인
print(df.info())

