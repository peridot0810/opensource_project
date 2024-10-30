# opensource_project
virtual try on 관련 전체 코드는 아래 레포지토리에 있음. 현재 opensource_project 레포지토리에는 일부만 존재
https://github.com/sebinyday/IDM-VTON 
## 코드 실행
1. 가상환경 생성 후 requirements.txt 설치
2. app.py 실행


## 회원가입
- 차례대로 입력 (이미지 업로드는 선택사항)
- firebase의 Realtime Database에 유저 정보 저장
  - 이미지는 /static/user_img 디렉토리에 저장, 이미지 path가 유저 정보에 저장됨 
- firebase 데이터베이스에 등록된 사용자는 로그인 가능


## 관리자 계정
- 관리자 : user id(uid)가 "root"인 회원
- 현재는 uid, pwd, name 모두 root로 등록되어있음 
- 로그인 안되면 uid "root"로 회원가입하기

### 관리자 권한 1 : 제품 등록
- 차례대로 입력 -> 유저 정보처럼 firebase에 저장됨
- 새로 등록된 제품은 홈페이지에 추가됨
- **주의 : 제품 이미지는 "static/product_img/ 위치에 "(product id).jpg" 형태로 저장되어있어야 페이지에 반영됨**

### 관리자 권한 2 : 유저/제품 삭제
- 유저관리/제품관리 페이지에서 유저 또는 제품 삭제 가능
- 삭제된 유저/제품은 firebase 데이터베이스에서 제거
- 유저의 경우 이미지까지(로컬의 /static/user_img/'유저이미지') 같이 삭제됨
- 제품의 이미지는 삭제되지 않음

## 옷 입어보기
- 제품 상세페이지에 '이 옷 입어보기' 클릭 -> try on 페이지로 넘어감
- 회원가입 할때 이미지를 업로드 하지 않았다면 업로드 화면으로 넘어감
 
