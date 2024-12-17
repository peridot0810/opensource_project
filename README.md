# FitME

## 코드 실행
1. clone 하기 
```bash
$ git clone https://github.com/2024-SSU-OpenSource-team10/FitMe
```

2. FitMe 디렉토리 진입
```bash
$ cd FitMe
```

3. 가상환경 생성 및 실행
```bash
$ conda create -n {가상환경 이름} python=3.12
$ conda activate {가상환경 이름}
```

4. 필요한 패키지 설치
```bash
$ pip install -r requirements.txt
```

5. 서버 실행
```bash
$ python3 app.py
```
6. FitMe 페이지 접속 : http://127.0.0.1:8080/

7. 새로운 터미널에서 VTON 폴더 진입 
```bash
$ cd VTON
```

8. 가상환경 실행
```bash
$ conda activate {가상환경 이름}
```

9. VTON 서버 실행
```bash
$ python3 app.py
```

## 회원가입
- 일반 사용자(consumer), 디자이너(designer)중 택1
  
### consumer
- 차례대로 입력 (이미지 업로드는 선택사항)
- firebase의 Realtime Database-'Consumers'에 정보 저장
	-  이미지는 로컬의 /static/consumer_img 디렉토리에 저장, 이미지 path가 유저 정보에 저장됨 

### designer
- 차례대로 입력
- firebase의 Realtime Database-'Designers'에 정보 저장
	- 로컬의 /static/designer_products 디렉토리에 해당 디자이너의 디렉토리 추가
	- 디자이너가 제품 등록 시 제품 이미지가 저장됨
- designer의 경우 홈페이지에 쇼핑몰 제품이 아닌, 본인이 등록한 제품이 보이게 됨
- 제품 등록 : 우측 상단 "제품 등록" 클릭, 제품 정보 입력 후 등록
- 제품 삭제 : 제품 상세 페이지에서 "제품 삭제하기" 클릭


## 마이 페이지
- 우측 상단에 사람 모양 클릭
- 비밀번호 수정 가능
- Consumer의 경우 이미지 수정 가능
  

## 옷 입어보기
- 제품 상세페이지에 'Virtual Try on' 클릭 -> try on 페이지로 넘어감
- 회원가입 할때 이미지를 업로드 하지 않았다면 마이페이지로 넘어감
- designer의 경우, 모델 이미지도 직접 입력

## 최종 시연 영상
https://youtu.be/OxibUSB8Bfs 

## 최종 보고서
[10조 최종 발표 보고서_FitMe.pdf](https://github.com/user-attachments/files/18167409/10._FitMe.pdf)
