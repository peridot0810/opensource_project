from flask import Flask, redirect, render_template, url_for, request, flash, session
from DB import DBModule
from Users import Consumer, Designer, Root
from Server import Server
from Products import Product
import os

# ==== 초기 설정 ====
app = Flask(__name__)
app.secret_key = os.urandom(24)      # 랜덤 secret key -> 서버 시작할때마다 세션 초기화
Server = Server()                    # Server 인스턴스 생성
# =================



# ===== 메인 페이지 =====
@app.route("/")
def index():
  try:
    user = Server.check_login()
    user_id = user.id
    user_type = user.type
  except:
    user_id = "Login_needed"
    user_type = None

  products = Server.get_products()

  if not products:                   # product가 없음 -> 제품 가져오기 실패
    products = "No_products"

  return render_template("index.html", user = user_id, type = user_type, products = products)  # index.html에 user, products 넘기기
# =====================



# ========= 마이 페이지 ===========
@app.route("/my_page")
def my_page():
  try:
    user = Server.check_login()
  except Exception as e:
    print(e)
    return redirect(url_for("login_userType"))
  
  user_info = Server.get_user_detail(user.id, user.type)
  
  return render_template("my_page.html", user_info = user_info, user_type=user.type)
# ===============================
  


# ========= 내 정보 수정 ============
@app.route("/edit_info")
def edit_info():
  try:
    user = Server.check_login()
  except:
    return redirect(url_for("login_userType"))
  
  user_info = {
    'id' : user.id,
    'name' : user.name,
    'pwd' : user.pwd,
    'type' : user.type
  }  

  if user.type == "Consumer":
    user_info["img_path"] = user.img_path
    return render_template("edit_info_consumer.html", user_info = user_info)
  if user.type == "Designer":
    user_info["img_path"] = user.dir_path
    return render_template("edit_info_designer.html", user_info = user_info)
  

@app.route("/edit_done", methods=["post"])  
def edit_done():
  try:
    user = Server.check_login()
  except:
    return redirect(url_for("index"))
  
  update_info = {
    "id" : request.form.get("id"),
    "pwd" : request.form.get("pwd"),
    "name" : request.form.get("name")
  }

  if Server.edit_info(user.id, user.type, update_info): # 정보 수정 성공
    return redirect(url_for("my_page"))    
  else:
    flash("정보 수정 실패")                                # 정보 수정 실패
    return redirect(url_for("edit_info"))
# ===============================



# ===== 회원가입 =====
@app.route("/signin_userType")
def signin_userType():                           # Designer, Consumer 구분
  try:
    Server.check_login()                  # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    return render_template("signin_userType.html")


@app.route("/signin", methods=["post"]) 
def signin():
  try:
    Server.check_login()                      # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    type = request.form.get("type")

    if type == "Consumer" :    # 일반 사용자 -> 일반 가입 페이지
      return render_template("signin_consumer.html")
    elif type == "Designer":   # 디자이너 사용자 -> 디자이너 가입 페이지
      return render_template("signin_designer.html")  
    elif type == "Root":       # 관리자
      return render_template("signin_root.html")                                   


@app.route("/signin_done", methods=["post"])  
def signin_done():
  try:
    Server.check_login()                    # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
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
  try:
    Server.check_login()                     # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    return render_template("login_userType.html")

@app.route("/login", methods=["post"]) 
def login():
  try:
    Server.check_login()                # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    return render_template("login.html", type = request.form.get("type"))

@app.route("/login_done", methods=["post"])  
def login_done():
  try:
    Server.check_login()                     # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
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
  try:
    Server.check_login()                      
    Server.log_out()
    return redirect(url_for("index"))
  except:                                          # 로그인 상태가 아니라면 redirect -> 로그인 창
    return redirect(url_for("login_userType"))
# =================================
  


# ========= 제품 등록 : Root ==========
@app.route("/product_registration")  
def product_registration():
  try:
    user = Server.check_login()
    user_type = user.type
  except:                                              # 로그인 상태가 아닌 경우
    user_type = None

  if user_type == "Root":
    return render_template("product_registration.html")
  else : 
    return redirect(url_for("index"))

@app.route("/registration_done", methods=["post"])  
def registration_done():
  product_info = {
    "pid" : request.form.get("id") ,
    "category" : request.form.get("category") ,
    "price" : request.form.get("price") ,
    "product_name" : request.form.get("name") ,
    "product_explain" : request.form.get("product_explain")  
  }
  product_img = request.files['product_img']
  category = request.form.get("category")

  if Server.product_registration(product_info, product_img, "Root", category=category):  # 제품 등록 성공
    return redirect(url_for("index"))
  else:                                                  # 제품 등록 실패
    flash("제품 ID가 중복됩니다")
    return redirect(url_for("product_registration"))
# ==============================



# ======= 제품 등록 : Designer ========
@app.route("/upload_product")
def upload_product():
  try:
    user = Server.check_login()
    if user.type == "Designer":
      return render_template("upload_product.html", did=user.id)
    else:
      return redirect(url_for("index"))
  except:
    return redirect(url_for("index"))

@app.route("/upload_product_done/<string:did>", methods=["post"])
def upload_product_done(did):
  product_img = request.files['product_img']
  product_info = {
    "product_name" : request.form.get("name"),
    "product_explain" : request.form.get("product_explain")
  }
  if Server.product_registration(product_info, product_img, "Designer", did=did): 
    return redirect(url_for("index"))
  else:
    flash("제품명이 중복되거나 이미지가 업로드되지 않았습니다")                 
    return redirect(url_for("upload_product", did=did))
# ==========================================



# ===== 개별 제품 상세정보 =====
@app.route("/product_detail")  # /product_detail/제품 ID
def product_detail():
  try:
    user = Server.check_login()
    user_type = user.type
  except:
    user_type = None

  pid = request.args.get("pid")
  if user_type == "Designer":
    product_info = Server.get_product_detail(pid, did=user.id)
  else:
    product_info = Server.get_product_detail(pid)
  return render_template("product_detail.html", product_info=product_info, user_type=user_type, pid=pid)
# ==========================



# ====== 관리 페이지 =======
@app.route("/user_manage")       
def user_manage():
  try:
    user = Server.check_login()
    user_type = user.type
  except:                                              # 로그인 상태가 아닌 경우
    user_type = None

  if user_type == "Root":
    consumers = Server.get_users("Consumer")
    designers = Server.get_users("Designer")
    return render_template("user_manage.html", consumers=consumers, designers=designers)
  else:
    return redirect(url_for("index"))

@app.route("/product_manage")   # url을 세부사항으로 분리해야할듯!    
def product_manage():
  try:
    user = Server.check_login()
    user_type = user.type
  except:                                              # 로그인 상태가 아닌 경우
    user_type = None

  if user_type == "Root":
    products = Server.get_products()
    return render_template("product_manage.html", products = products)
  else:
    return redirect(url_for("index"))
# =========================




# ======= 관리(삭제) 페이지 ========
@app.route("/user_delete")       
def user_delete():
  try:
    user = Server.check_login()
    user_id = user.id
    user_type = user.type
  except:                                              # 로그인 상태가 아닌 경우
    user_id, user_type = (None, None)

  if user_type == "Root":
    type = request.args.get('type')
    id = request.args.get('uid')
    Server.user_delete(type, id)
    return redirect(url_for("user_manage"))
  else:
    return redirect(url_for("index"))
  

@app.route("/product_delete")       
def product_delete():
  try:
    user = Server.check_login()
    user_type = user.type
  except:                                              # 로그인 상태가 아닌 경우
    user_type = None

  pid = request.args.get('pid')
  if user_type == "Root":
    
    Server.product_delete("Root", pid)
    return redirect(url_for("product_manage"))
  elif user_type == "Designer":
    Server.product_delete("Designer", pid, did=user.id)
    return redirect(url_for("index"))
  else:
    return redirect(url_for("index"))
# ================================



# ========== 옷 입어보기 =============
@app.route("/try_on")
def try_on():
  try:
    user = Server.check_login()
  except:
    return redirect(url_for("login_userType"))
  
  pid = request.args.get("pid")

  product_info = Server.get_product_detail(pid)
  product_img_path = product_info["img_path"]
  if user.img_path == "No_img":
    flash("해당 서비스 이용을 위해서는 사진 업로드가 필요합니다") 
    return redirect(url_for("upload_img", cid=user.id))
  return render_template("try_on.html", model_img_path=user.img_path, product_img_path=product_img_path)

@app.route("/upload_img/<string:cid>")        # 회원가입때 이미지를 업로드하지 않은 경우
def upload_img(cid):
  return render_template("upload_img.html", cid=cid)

@app.route("/upload_done", methods=["post"])
def upload_done():
  img = None
  cid = request.args.get("cid")
  if 'consumer_img' in request.files:
    img = request.files['consumer_img']
  if Server.upload_img(img, cid): 
    return redirect(url_for("index"))
  else:
    flash("업로드에 실패했습니다")                  # 이미지를 업로드 하지 않은 채 제출한 경우
    return redirect(url_for("upload_img", cid=cid))
# ================================



# ===== 서버 실행 =====
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True)


