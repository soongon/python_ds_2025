import requests
from bs4 import BeautifulSoup
import pandas as pd

# 상수 선언
URL = "https://www.coupang.com/np/campaigns/82/components/194176"  # 쿠팡 로켓배송 식품 카테고리 URL
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Connection": "keep-alive"
}

# 함수 정의

def fetch_html(url, headers):
    """지정된 URL에서 HTML을 가져옵니다."""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # HTTP 응답 상태 코드 확인
        return response.text  # HTML 반환
    except requests.exceptions.RequestException as e:
        print(f"HTTP 요청 중 오류 발생: {e}")
        return None

def parse_products(html):
    """HTML에서 상품 정보를 파싱합니다."""
    soup = BeautifulSoup(html, "html.parser")
    products = soup.find_all("li", class_="baby-product")  # 상품 리스트 요소 찾기
    product_list = []

    for product in products:
        try:
            # 상품명 가져오기
            name = product.find("div", class_="name").get_text(strip=True)

            # 가격 가져오기 (콤마 제거 후 숫자로 변환)
            price = int(product.find("strong", class_="price-value").get_text(strip=True).replace(",", ""))

            # 평점 가져오기 (평점이 없으면 0.0으로 설정)
            rating_tag = product.find("em", class_="rating")
            rating = float(rating_tag.get_text(strip=True)) if rating_tag else 0.0

            # 이미지 URL 가져오기
            image_tag = product.find("img")
            image_url = image_tag["src"] if image_tag else "N/A"

            # 결과 리스트에 추가
            product_list.append({
                "상품명": name,
                "가격": price,
                "평점": rating,
                "이미지 URL": image_url
            })
        except AttributeError as e:
            print(f"상품 데이터 추출 중 오류 발생: {e}")
    return product_list

def save_to_excel(data, filename):
    """상품 데이터를 엑셀 파일로 저장합니다."""
    try:
        df = pd.DataFrame(data)  # 데이터프레임 생성
        df.to_excel(filename, index=False)  # 엑셀 파일로 저장
        print(f"데이터가 {filename} 파일로 저장되었습니다!")
    except Exception as e:
        print(f"엑셀 저장 중 오류 발생: {e}")

# 메인 실행
if __name__ == "__main__":
    html = fetch_html(URL, HEADERS)  # HTML 가져오기
    if html:
        products = parse_products(html)  # 상품 정보 파싱
        if products:
            save_to_excel(products, "coupang_products.xlsx")  # 엑셀 파일 저장
