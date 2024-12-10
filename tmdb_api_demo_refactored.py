import requests
import pandas as pd

# API URL 및 헤더 설정
API_URL = "https://api.themoviedb.org/3/movie/now_playing?language=ko-KR&page=1&region=kr"
HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MDM3YTAwN2ZhMmE5MzM1NTdmNWYyMzBlMGYyZTYwZiIsIm5iZiI6MTY4Nzc2MzE4MS4zODUsInN1YiI6IjY0OTkzOGVkNmY0M2VjMDBjNWM3MmY4NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c36HQAp9HEFqYlAdtspic4Deb284ZTrc-YGOliBHkuk"
}


# 영화 데이터를 가져오는 함수
def fetch_now_playing_movies(api_url, headers):
    """
    현재 상영 중인 영화 데이터를 API에서 가져옴.

    :param api_url: API 호출을 위한 URL
    :param headers: API 인증 및 설정을 위한 헤더
    :return: 영화 데이터 리스트 (성공 시), None (실패 시)
    """
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # HTTP 에러 발생 시 예외 처리
        return response.json().get('results', [])  # 'results' 키의 값 반환
    except requests.exceptions.RequestException as e:
        print(f"API 요청 실패: {e}")
        return None


# 영화 데이터를 DataFrame으로 변환하는 함수
def transform_movies_to_dataframe(movies):
    """
    영화 데이터를 pandas DataFrame으로 변환.

    :param movies: 영화 데이터 리스트
    :return: 변환된 pandas DataFrame
    """
    return pd.DataFrame(
        [[movie.get('title'), movie.get('overview'), movie.get('vote_average'), movie.get('release_date')]
         for movie in movies],
        columns=["제목", "줄거리", "평점", "개봉일"]
    )


# DataFrame을 엑셀 파일로 저장하는 함수
def save_dataframe_to_excel(df, filename):
    """
    DataFrame을 엑셀 파일로 저장.

    :param df: 저장할 pandas DataFrame
    :param filename: 저장할 파일 이름
    """
    try:
        df.to_excel(filename, index=False)
        print(f"엑셀 파일 저장 완료: {filename}")
    except Exception as e:
        print(f"엑셀 저장 실패: {e}")


# 메인 로직
def main():
    # 1. 영화 데이터 가져오기
    movies = fetch_now_playing_movies(API_URL, HEADERS)
    if movies is None:
        print("영화 데이터를 가져오지 못했습니다. 프로그램을 종료합니다.")
        return

    # 2. 영화 데이터를 DataFrame으로 변환
    df = transform_movies_to_dataframe(movies)

    # 3. DataFrame을 엑셀 파일로 저장
    save_dataframe_to_excel(df, "now_playing_movies.xlsx")


# 프로그램 실행
if __name__ == "__main__":
    main()
