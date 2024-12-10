import requests
import pandas as pd

url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-KR&page=1&region=kr"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MDM3YTAwN2ZhMmE5MzM1NTdmNWYyMzBlMGYyZTYwZiIsIm5iZiI6MTY4Nzc2MzE4MS4zODUsInN1YiI6IjY0OTkzOGVkNmY0M2VjMDBjNWM3MmY4NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c36HQAp9HEFqYlAdtspic4Deb284ZTrc-YGOliBHkuk"
}

response = requests.get(url, headers=headers)

movies = []
for movie in response.json().get('results'):
    movies.append([ movie.get('title'),
      movie.get('overview'),
      movie.get('vote_average'),
      movie.get('release_date') ])

# 이중 리스트를 엑셀로 저장
df = pd.DataFrame(movies, columns=["제목", "줄거리", "평점", "개봉일"])
df.to_excel('now_playing_movies.xlsx', index=False)
print('job completed..')
