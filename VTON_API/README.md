# VTON Virtual Try-On Setup Guide

이 가이드는 `VTON` 가상 착용 프로젝트를 설정하고 실행하는 방법을 설명합니다. Python 가상환경, Gradio 클라이언트 및 필수 파일 설정 단계를 포함합니다.

## 사전 요구 사항
- Anaconda (또는 Miniconda)
- Python 3.10

## 설치 및 실행 방법

### 1. VTON 디렉토리 생성
작업할 프로젝트 디렉토리를 생성하고 해당 디렉토리로 이동합니다.

```bash
mkdir VTON
cd VTON
```
### 2. Conda 가상환경 생성 및 활성화
Python 3.10 버전을 사용하여 vton 가상환경을 생성하고 활성화합니다.
```bash
conda create -n vton python=3.10
conda activate vton
```
### 3. Gradio 클라이언트 및 Pillow 설치
필요한 패키지를 설치합니다.
```bash
pip install gradio_client Pillow
```

### 4. 파일 준비
#### 4-1. jpg2png
이미지 변환 스크립트: jpg2png.py를 생성하여 JPEG 파일을 PNG로 변환합니다.
```bash
touch jpg2png.py
```
```python
import os
from PIL import Image

input_dir = "경로/VTON/garment_image"

for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):
        jpg_path = os.path.join(input_dir, filename)
        png_path = os.path.join(input_dir, os.path.splitext(filename)[0] + ".png")

        with Image.open(jpg_path) as img:
            img.save(png_path, "PNG")
        
        os.remove(jpg_path)

print("모든 JPG 파일이 PNG로 변환되고 원본 JPG 파일이 삭제되었습니다.")

```
#### 4-2. run
API 실행 스크립트: `run.py`를 생성하여 API를 호출하고 결과를 출력합니다.
```bash
touch run.py
```
`run.py` 파일을 열고 다음 코드를 추가합니다. 이 코드는 Gradio Client를 통해 가상 착용 API에 요청을 보내고 결과를 출력합니다.
```python
import os
os.environ["TMPDIR"] = "임시경로/VTON/tmp"

from gradio_client import Client, file

client = Client("Nymbo/Virtual-Try-On")

result = client.predict(
    dict={"background": file('./background_image/001-woman.png'), "layers": [], "composite": None},
    garm_img=file('./garment_image/001-pink_hoodie.png'),
    garment_des="Hello!!",
    is_checked=True,
    is_checked_crop=False,
    denoise_steps=30,
    seed=42,
    api_name="/tryon"
)
print(result)
```

### 5. 스크립트 실행
모든 준비가 완료되면 아래 명령어로 스크립트를 실행합니다.
```bash
# JPG 파일을 PNG로 변환
python jpg2png.py

# 가상 착용 API 호출
python run.py
```

### 문제 해결
- Permission Error: 임시 디렉토리 권한 문제 발생 시 run.py에서 설정한 TMPDIR 경로가 쓰기 가능하도록 설정하세요.
- file() 경고: 최신 Gradio 버전에서는 file() 대신 handle_file() 사용을 권장합니다.
- 필요한 이미지 파일을 적절한 경로에 배치해야합니다. 