# from bs4 import BeautifulSoup 
# import time
# import urllib.request as req
# import os

# num_page = 100
# save_dir = "./img"
# for page in range(1,num_page):
#     # page 변경
#     url = "https://search.musinsa.com/category/001?device=&d_cat_cd=001&brand=&rate=&page_kind=search&list_kind=big&sort=pop&sub_sort=&page={}".format(page)
#     res = req.urlopen(url)

#     soup = BeautifulSoup(res, "html.parser")
#     # img 태그 리스트
#     img_list = soup.select("div.list_img.articleImg > a > img")
#     clothes_num = 1
#     for img in img_list:
#         # data-original = 이미지 경로
#         img_url = img.attrs['data-original']
#         savename = "{}/{}_page_{}clothes.png".format(save_dir, page, clothes_num);
#         clothes_num += 1
#         req.urlretrieve(img_url, savename)
#         print(savename, "저장 완료!")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import time

# ChromeDriver 경로 설정
chrome_service = Service('"C:\Users\jnf02\Downloads\chromedriver_win32\chromedriver.exe"')  # 여기에 chromedriver 경로를 입력하세요.
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 백그라운드에서 실행
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Selenium을 사용하여 페이지 로드
driver = webdriver.Chrome(service=chrome_service, options=options)
url = "https://www.musinsa.com/category/001?gf=A"
driver.get(url)

# 페이지가 로드되기를 기다림
time.sleep(3)  # 필요에 따라 시간을 조정하세요.

# 페이지 소스를 BeautifulSoup로 파싱
soup = BeautifulSoup(driver.page_source, 'html.parser')

# `max-w-full w-full absolute m-auto inset-0 h-auto z-0 visible object-contain` 클래스가 적용된 이미지 태그 찾기
image_tags = soup.find_all('img', class_="max-w-full w-full absolute m-auto inset-0 h-auto z-0 visible object-contain")

# 조건을 만족하는 이미지 URL을 저장할 리스트
filtered_image_urls = []

# 이미지 URL 추출 및 필터링
for img_tag in image_tags:
    img_url = img_tag.get('src')
    if img_url:
        try:
            # 이미지 다운로드
            img_response = requests.get(img_url)
            img = Image.open(BytesIO(img_response.content))
            
            # 이미지가 충분히 큰지 확인 (780x780 이상이어야 함)
            if img.width >= 780 and img.height >= 780:
                # (0,0)과 (780,780) 픽셀 색상 추출
                pixel_0_0 = img.getpixel((0, 0))
                pixel_780_780 = img.getpixel((780, 780))
                
                # 두 픽셀이 같은지 확인
                if pixel_0_0 == pixel_780_780:
                    # 조건을 만족하는 경우 리스트에 추가
                    filtered_image_urls.append(img_url)
                    print(f"Added image: {img_url}")
                else:
                    print("누끼이미지가 아님")
            else:
                print("이미지 크기 780 이하임")
        
        except Exception as e:
            print(f"Error processing image {img_url}: {e}")
    else:
        print("img_url 없음")

# 드라이버 종료
driver.quit()

# 결과 출력
print("조건을 만족하는 이미지 URL 개수:", len(filtered_image_urls))
for idx, img_url in enumerate(filtered_image_urls, start=1):
    print(f"{idx}: {img_url}")
