from flask import Flask, redirect, render_template, url_for, request, flash, session
from DB import DBModule
from Users import Consumer, Designer, Root
from Server import Server
from Products import Product
import os

# ==== 초기 설정 ====
app = Flask(__name__)
app.secret_key = os.urandom(24)      # 랜덤 secret key -> 서버 시작할때마다 세션 초기화
# DB = DBModule()                    # DB모듈 인스턴스 생성
Server = Server()                    # Server 인스턴스 생성
# =================



# ===== 메인 페이지 =====
@app.route("/")
def index():
  try:
    user, user_type = Server.check_login()
  except:
    user = "Login_needed"
    user_type = None

  products = Server.get_products()

  if not products:                   # product가 없음 -> 제품 가져오기 실패
    products = "No_products"
  return render_template("index.html", user = user, type = user_type, products = products)  # index.html에 user, products 넘기기
# =====================



# ========= 마이 페이지 ===========
@app.route("/my_page")
def my_page():
  try:
    user, user_type = Server.check_login()
  except:
    return redirect(url_for("login_userType"))
  
  user_info = Server.get_user_detail(user, user_type)
  
  return render_template("my_page.html", user_info = user_info, user_type=user_type)
# ===============================
  


# ========= 내 정보 수정 ============
@app.route("/edit_info")
def edit_info():
  try:
    user, user_type = Server.check_login()
  except:
    return redirect(url_for("login_userType"))
  
  user_info = Server.get_user_detail(user, user_type)

  if user_type == "Consumer":
    return render_template("edit_info_consumer.html", user_info = user_info)
  if user_type == "Designer":
    return render_template("edit_info_designer.html", user_info = user_info)
  

@app.route("/edit_done", methods=["post"])  
def edit_done():
  try:
    user, user_type = Server.check_login()
  except:
    return redirect(url_for("index"))
  
  update_info = {
    "id" : request.form.get("id"),
    "pwd" : request.form.get("pwd"),
    "name" : request.form.get("name")
  }

  if Server.edit_info(user, user_type, update_info): # 정보 수정 성공
    return redirect(url_for("my_page"))    
  else:
    flash("정보 수정 실패")                              # 정보 수정 실패
    return redirect(url_for("edit_info"))
# ===============================



# ===== 회원가입 =====
@app.route("/signin_userType")
def signin_userType():                           # Designer, Consumer 구분
  if Server.check_login():                       # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  return render_template("signin_userType.html")


@app.route("/signin", methods=["post"]) 
def signin():
  if Server.check_login():                       # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  
  type = request.form.get("type")

  if type == "Consumer" :    # 일반 사용자 -> 일반 가입 페이지
    return render_template("signin_consumer.html")
  elif type == "Designer":   # 디자이너 사용자 -> 디자이너 가입 페이지
    return render_template("signin_designer.html")  
  elif type == "Root":       # 관리자
    return render_template("signin_root.html")                                   


@app.route("/signin_done", methods=["post"])  
def signin_done():
  if Server.check_login():                       # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  
  user_info = {
    "id" : request.form.get("id"),
    "pwd" : request.form.get("pwd"),
    "name" : request.form.get("name"),
    "type" : request.form.get("type")
  }

  if user_info["type"] == "Consumer" and 'consumer_img' in request.files:
    img = request.files['consumer_img']
  else:
    img = None

  if Server.sign_in(user_info, img):                 # 회원가입 성공
    return redirect(url_for("login_userType"))    
  else:
    flash("이미 존재하는 아이디 입니다")                    # 회원가입 실패
    return redirect(url_for("signin_userType"))
# ======================



# ===== 로그인/로그아웃 =====
@app.route("/login_userType")
def login_userType():                            # 디자이너인지 소비자인지 구분
  if Server.check_login():                       # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  return render_template("login_userType.html")

@app.route("/login", methods=["post"]) 
def login():
  if Server.check_login():                       # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  return render_template("login.html", type = request.form.get("type"))

@app.route("/login_done", methods=["post"])  
def login_done():
  if Server.check_login():                       # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  login_info = {
    "id" : request.form.get("id"),
    "pwd" : request.form.get("pwd"),
    "type" : request.form.get("type")
  }
  if Server.log_in(login_info):                  # 로그인 성공 -> session["id"] = 유저 아이디
    return redirect(url_for("index"))
  else:                                          # 로그인 실패
    flash("아이디가 없거나 틀린 비밀번호 입니다")
    return redirect(url_for("login_userType"))

@app.route("/logout")
def logout():
  if Server.check_login():                       # 로그인 상태라면 session에서 "id", "type"이라는 key를 pop
    Server.log_out()
    return redirect(url_for("index"))
  else:                                          # 로그인 상태가 아니라면 redirect -> 로그인 창
    return redirect(url_for("login_userType"))
# =================================
  


# ========= 제품 등록 ==========

# ==============================


# ====== 관리 페이지 =======
@app.route("/user_manage")       
def user_manage():
  try:
    user, user_type = Server.check_login()
  except:                                              # 로그인 상태가 아닌 경우
    user, user_type = (None, None)

  if user_type == "Root":
    consumers = Server.get_users("Consumer")
    designers = Server.get_users("Designer")
    return render_template("user_manage.html", consumers=consumers, designers=designers)
  else:
    return redirect(url_for("index"))

@app.route("/product_manage")       
def product_manage():
  pass
# =========================




# ======= 관리(삭제) 페이지 ========
@app.route("/user_delete")       
def user_delete():
  try:
    user, user_type = Server.check_login()
  except:                                              # 로그인 상태가 아닌 경우
    user, user_type = (None, None)

  if user_type == "Root":
    type = request.args.get('type')
    id = request.args.get('uid')
    Server.user_delete(type, id)
    return redirect(url_for("user_manage"))
  else:
    return redirect(url_for("index"))
  

@app.route("/product_delete")       
def product_delete():
  pass
# ================================





# ===== 서버 실행 =====
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True)


