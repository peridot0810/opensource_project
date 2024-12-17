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
 


## 관리자 계정
- 관리자 : 로그인 시 '관리자' 선택하여 로그인 가능
- 현재는 id, pwd, name 모두 root로 등록되어있음 
- 로그인 안되면 '관리자'회원, id "root", pwd "root"로 회원가입하기

### 관리자 권한 1 : 제품 등록
- 로컬의 products_to_register 디렉토리에 등록할 제품 이미지 저장
- 제품 등록 페이지에서 차례대로 입력 
- firebase의 Realtime Database-'Products'에 정보 저장
- 새로 등록된 제품은 홈페이지에 추가됨
- 제품 이미지는 로컬의 static/product_img에 저장됨 

### 관리자 권한 2 : 유저/제품 삭제
- 유저관리/제품관리 페이지에서 유저 또는 제품 삭제 가능
- 삭제된 유저/제품은 firebase 데이터베이스에서 제거
- 로컬에 저장되어있는 유저/제품의 이미지도 삭제됨

## 옷 입어보기
- 제품 상세페이지에 '이 옷 입어보기' 클릭 -> try on 페이지로 넘어감
- 회원가입 할때 이미지를 업로드 하지 않았다면 업로드 화면으로 넘어감

## 피그마 시연 영상
https://github.com/user-attachments/assets/45cc5aa9-7505-4a37-a6ff-209dd40726f8

