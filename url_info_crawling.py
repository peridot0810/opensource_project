from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import time
import os
import re
import csv

# ChromeDriver 경로 설정
chrome_service = Service("C:\\Users\\jnf02\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 백그라운드에서 실행
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


# Selenium을 사용하여 페이지 로드
driver = webdriver.Chrome(service=chrome_service, options=options)
#url = "https://www.musinsa.com/category/001?gf=A"
#url = "https://www.musinsa.com/category/002?gf=A"
#url = "https://www.musinsa.com/category/003?gf=A"
url = "https://www.musinsa.com/category/100?gf=A"
driver.get(url)

# 페이지 스크롤을 통한 추가 이미지 로드
SCROLL_PAUSE_TIME = 2
for _ in range(50):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

# 페이지 소스를 BeautifulSoup로 파싱
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 상품 정보 수집
product_data = []
product_tags = soup.find_all('a', class_="gtm-select-item")

for product in product_tags:
    product_name = product.get('aria-label')  # 상품 이름
    product_url = product.get('href')  # 상품 URL (상대 경로)
    discount_rate = product.get('data-discount-rate')  # 할인율
    original_price = product.get('data-original-price')  # 정가
    discounted_price = product.get('data-price')  # 할인가
    
    # 이미지 URL 추출
    img_tag = product.find_previous("img")  # <a> 태그 이전의 <img> 태그 찾기
    img_url = img_tag["src"] if img_tag else None

    if product_name and product_url and img_url:
        # 수집한 정보 저장
        product_data.append({
            "name": product_name,
            "url": img_url,  # 이미지의 URL을 사용
            "discount_rate": discount_rate + "%" if discount_rate else "0%",
            "original_price": f"{original_price}원" if original_price else "가격 없음",
            "discounted_price": f"{discounted_price}원" if discounted_price else "가격 없음",
        })

# CSV 파일로 저장
with open("product_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "url", "discount_rate", "original_price", "discounted_price"])
    writer.writeheader()
    writer.writerows(product_data)

driver.quit()
print("CSV 파일 저장 완료: product_data.csv")
# # Selenium을 사용하여 페이지 로드
# driver = webdriver.Chrome(service=chrome_service, options=options)
# url = "https://www.musinsa.com/category/001?gf=A"
# driver.get(url)

# # 페이지 스크롤을 통한 추가 이미지 로드
# SCROLL_PAUSE_TIME = 2
# for _ in range(50):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)

# # 페이지 소스를 BeautifulSoup로 파싱
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # 상품 정보 수집
# product_data = []
# product_tags = soup.find_all('a', class_="gtm-select-item")

# for product in product_tags:
#     product_name = product.get('aria-label')  # 상품 이름
#     product_url = product.get('href')  # 상품 URL (상대 경로)
#     discount_rate = product.get('data-discount-rate')  # 할인율
#     original_price = product.get('data-original-price')  # 정가
#     discounted_price = product.get('data-price')  # 할인가

#     if product_name and product_url:
#         # 수집한 정보 저장
#         product_data.append({
#             "name": product_name,
#             "url": product_url,  # 전체 URL로 만들지 않고 상대 경로만 저장
#             "discount_rate": discount_rate + "%" if discount_rate else "0%",
#             "original_price": f"{original_price}원" if original_price else "가격 없음",
#             "discounted_price": f"{discounted_price}원" if discounted_price else "가격 없음",
#         })

# # CSV 파일로 저장
# with open("product_data.csv", mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "url", "discount_rate", "original_price", "discounted_price"])
#     writer.writeheader()
#     writer.writerows(product_data)

# driver.quit()
# print("CSV 파일 저장 완료: product_data.csv")

# # Selenium을 사용하여 페이지 로드
# driver = webdriver.Chrome(service=chrome_service, options=options)

# url = "https://www.musinsa.com/category/001?gf=A"
# driver.get(url)

# # 페이지 스크롤을 통한 추가 이미지 로드
# SCROLL_PAUSE_TIME = 2
# for _ in range(50):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)

# # 페이지 소스를 BeautifulSoup로 파싱
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # 상품 정보 수집
# product_data = []
# product_tags = soup.find_all('a', class_="gtm-select-item")

# for product in product_tags:
#     product_name = product.get('aria-label')  # 상품 이름
#     product_url = product.get('href')  # 상품 URL
#     discount_rate = product.get('data-discount-rate')  # 할인율
#     original_price = product.get('data-original-price')  # 정가
#     discounted_price = product.get('data-price')  # 할인가

#     if product_name and product_url:
#         # 수집한 정보 저장
#         product_data.append({
#             "name": product_name,
#             "url": f"https://www.musinsa.com{product_url}",
#             "discount_rate": discount_rate + "%" if discount_rate else "0%",
#             "original_price": f"{original_price}원" if original_price else "가격 없음",
#             "discounted_price": f"{discounted_price}원" if discounted_price else "가격 없음",
#         })

# # CSV 파일로 저장
# with open("product_data.csv", mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "url", "discount_rate", "original_price", "discounted_price"])
#     writer.writeheader()
#     writer.writerows(product_data)

# driver.quit()
# print("CSV 파일 저장 완료: product_data.csv")

# # 목표 배경색 (RGB 값)
# TARGET_COLOR = (245, 245, 245)
# TOLERANCE = 10
# SAVE_DIR = "C:\\Users\\jnf02\\OneDrive\\바탕 화면\\SSU3-2\\오픈소스기반기초설계\\dataset"  # 이미지를 저장할 디렉토리

# def is_similar_color(color1, color2, tolerance=TOLERANCE):
#     """두 색상의 차이가 tolerance 이내인지를 확인"""
#     return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

# def sanitize_filename(filename):
#     """파일명에서 공백은 '_'로 바꾸고, 특수 문자를 제거"""
#     return re.sub(r'[^A-Za-z0-9가-힣_]+', '', filename.replace(" ", "_"))

# # ChromeDriver 경로 설정
# chrome_service = Service("C:\\Users\\jnf02\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 백그라운드에서 실행
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')


# # Selenium을 사용하여 페이지 로드
# driver = webdriver.Chrome(service=chrome_service, options=options)
# url = "https://www.musinsa.com/category/001?gf=A"
# driver.get(url)

# # 페이지 스크롤을 통한 추가 이미지 로드
# SCROLL_PAUSE_TIME = 2
# last_height = driver.execute_script("return document.body.scrollHeight")

# # 지정된 스크롤 높이까지 반복하여 스크롤
# for _ in range(50):  # 더 많은 스크롤을 원하면 숫자를 늘려주세요
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:  # 더 이상 스크롤할 내용이 없으면 종료
#         break
#     last_height = new_height


# # 페이지 소스를 BeautifulSoup로 파싱
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # `max-w-full w-full absolute m-auto inset-0 h-auto z-0 visible object-contain` 클래스가 적용된 이미지 태그 찾기
# image_tags = soup.find_all('img', class_="max-w-full w-full absolute m-auto inset-0 h-auto z-0 visible object-contain")

# # 조건을 만족하는 이미지 URL을 저장할 리스트
# filtered_image_urls = []

# # 이미지 URL 추출 및 필터링
# for img_tag in image_tags:
#     img_url = img_tag.get('src')
#     img_alt = img_tag.get('alt')  # alt 속성에서 상품 이름 추출
#     if img_url and img_alt:
#         try:
#             # 이미지 다운로드
#             img_response = requests.get(img_url)
#             img = Image.open(BytesIO(img_response.content))
            
#             # 이미지 크기 확인 및 (0,0) 픽셀 색상 추출
#             if img.width >= 780 and img.height >= 780:
#                 pixel_0_0 = img.getpixel((0, 0))
                
#                 # (0,0) 픽셀이 목표 배경색에 유사한지 확인
#                 if is_similar_color(pixel_0_0, TARGET_COLOR):
#                     # 조건을 만족하는 경우 리스트에 추가
#                     filtered_image_urls.append(img_url)
#                     print(f"Added image: {img_url}")

#                      # 파일명 생성 (상품 이름을 사용)
#                     sanitized_name = sanitize_filename(img_alt)
#                     img_filename = os.path.join(SAVE_DIR, f"{sanitized_name}.jpg")
#                     img.save(img_filename)
#                     print(f"Image saved as: {img_filename}")

#                 else:
#                     print(f"{img_url}: 배경색이 #f5f5f5와 유사하지 않음")
#             else:
#                 print(f"{img_url}: 이미지 크기 780 이하임")
        
#         except Exception as e:
#             print(f"Error processing image {img_url}: {e}")
#     else:
#         print("img_url 없음")

# # 드라이버 종료
# driver.quit()

# # 결과 출력
# print("조건을 만족하는 이미지 URL 개수:", len(filtered_image_urls))
# for idx, img_url in enumerate(filtered_image_urls, start=1):
#     print(f"{idx}: {img_url}")