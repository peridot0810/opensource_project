from PIL import Image
from io import BytesIO
import requests
import csv
import os
import re

# 이미지 저장 디렉토리 설정
SAVE_DIR = "C:\\Users\\jnf02\\OneDrive\\바탕 화면\\SSU3-2\\오픈소스기반기초설계\\dataset"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def sanitize_filename(filename):
    """파일명에서 불필요한 문자 제거"""
    filename = filename.replace("상품상세로 이동", "").strip()  # "상품상세로 이동" 제거
    return re.sub(r'[^A-Za-z0-9가-힣_]+', '_', filename)

# CSV 파일을 읽고 이미지 다운로드
with open("product_data.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        img_url = row["url"]  # URL을 전체 경로로 변경
        img_name = sanitize_filename(row["name"])

        try:
            # 이미지 다운로드 및 저장
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            
            img_path = os.path.join(SAVE_DIR, f"{img_name}.jpg")
            img.save(img_path)
            print(f"Downloaded and saved: {img_path}")

        except Exception as e:
            print(f"Error downloading image {img_url}: {e}")
