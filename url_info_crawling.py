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
