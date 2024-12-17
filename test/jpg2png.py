import os
from PIL import Image

# 경로 설정
input_dir = "/home/her/s/VTON/garment_image"

# 경로에 있는 파일들을 반복
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):
        # 파일의 전체 경로
        jpg_path = os.path.join(input_dir, filename)
        
        # .png 형식으로 저장할 경로 설정
        png_path = os.path.join(input_dir, os.path.splitext(filename)[0] + ".png")
        
        # 이미지 열고 변환 후 저장
        with Image.open(jpg_path) as img:
            img.save(png_path, "PNG")
        
        # 변환 후 원래 jpg 파일 삭제
        os.remove(jpg_path)

print("모든 jpg 파일이 png로 변환되고 원본 jpg 파일이 삭제되었습니다.")
