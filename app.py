from flask import Flask, redirect, render_template, url_for, request, flash, session
from DB_handler import DBModule

# ==== 초기 설정 ====
app = Flask(__name__)
app.secret_key = "as;dlkjgao;psjr"   # 아무거나 친 코드. 유출되면 안됨
DB = DBModule()                      # DB모듈 인스턴스 생성
# =================



# ===== 메인 페이지 =====
@app.route("/")
def index():
  if "id" in session:                # 로그인이 되어있다면  -> user = 유저 아이디
    user = session['id']
    user_type = session['type']
  else:                              # 로그인되어있지 않다면 -> user = "Login_needed"
    user = "Login_needed"
    user_type = None

  if user_type == 'designer':
    products = DB.get_designer_products(user)
  else:
    products = DB.get_products()

  if not products:                   # product가 없음 -> 제품 가져오기 실패
    products = "No_products"
  return render_template("index.html", user = user, type = user_type, products = products)  # index.html에 user, products 넘기기
# =====================


# ========= 마이 페이지 ===========
@app.route("/my_page")
def my_page():
  if "id" in session:                # 로그인이 되어있다면  -> user = 유저 아이디
    user = session['id']
    type = session['type']
  else:                              # 로그인되어있지 않다면 -> 로그인 창으로 redirect
    return redirect(url_for("login_userType"))

  user_info = DB.get_user_detail(user, type)
  
  return render_template("my_page.html", user_info = user_info, user_type=type)
  
# ===============================
  





# ===== 회원가입 =====
@app.route("/signin_userType")
def signin_userType():                   # 디자이너인지 소비자인지 구분
  return render_template("signin_userType.html")


@app.route("/signin", methods=["post"]) 
def signin():
  if "id" in session:                       # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  if request.form.get("type") == "consumer" :    # 일반 사용자 -> 일반 가입 페이지
    return render_template("signin.html")
  else:                                      # 디자이너 사용자 -> 디자이너 가입 페이지
    return render_template("signin_designer.html")                                   


@app.route("/signin_done", methods=["post"])  
def signin_done():
  uid = request.form.get("id")
  pwd = request.form.get("pwd")
  name = request.form.get("name")
  type = request.form.get("type")
  img = None
  if 'consumer_img' in request.files:
    img = request.files['consumer_img']
  
  if DB.signin(uid, pwd, name, img, type):      # 회원가입 성공
    return redirect(url_for("login_userType"))
  else:
    flash("이미 존재하는 아이디 입니다")               # 회원가입 실패
    return redirect(url_for("signin_userType"))
# ======================



# ===== 로그인/로그아웃 =====
@app.route("/login_userType")
def login_userType():                   # 디자이너인지 소비자인지 구분
  return render_template("login_userType.html")

@app.route("/login", methods=["post"]) 
def login():
  if "id" in session:                # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  type = request.form.get("type")
  return render_template("login.html", type=type)

@app.route("/login_done", methods=["post"])  
def login_done():
  id = request.form.get("id")
  pwd = request.form.get("pwd")
  type = request.form.get("type")
  if DB.login(id, pwd, type):              # 로그인 성공 -> session["id"] = 유저 아이디
    session["id"] = id
    session["type"] = type
    return redirect(url_for("index"))
  else:                               # 로그인 실패
    flash("아이디가 없거나 틀린 비밀번호 입니다")
    return redirect(url_for("login_userType"))

@app.route("/logout")
def logout():
  if "id" in session:                # 로그인 상태라면 session에서 "id", "type"이라는 key를 pop
    session.pop("id")
    session.pop("type")
    return redirect(url_for("index"))
  else:                               # 로그인 상태가 아니라면 redirect -> 로그인 창
    return redirect(url_for("login_userType"))
# =================================
  


# ====== 제품 등록 ======
@app.route("/product_registration")  
def product_registration():
  if "id" not in session or session["id"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 제품 등록 가능 
    return redirect(url_for("index"))
  return render_template("product_registration.html")

@app.route("/registration_done", methods=["post"])  
def registration_done():
  pid = request.form.get("id")
  price = request.form.get("price")
  product_name = request.form.get("name")
  product_explain = request.form.get("product_explain")
  product_img = request.files['product_img']
  if DB.product_registration(pid, price, product_name, product_explain, product_img):  # 제품 등록 성공
    return redirect(url_for("index"))
  else:                                                  # 제품 등록 실패
    flash("제품 ID가 중복됩니다")
    return redirect(url_for("product_registration"))
# =======================



# ===== 개별 제품 상세정보 =====
@app.route("/product_detail/<string:pid>")  # /product_detail/제품 ID
def product_detail(pid):
  product_info = DB.get_product_detail(pid)
  return render_template("product_detail.html", product_info=product_info, pid=pid)
# ==========================



# ===== 옷 입어보기 ======
@app.route("/try_on/<string:pid>")
def try_on(pid):
  if "id" not in session:
    flash("로그인이 필요한 서비스입니다") 
    return redirect(url_for("login"))
  cid = session["id"]
  type = session["type"]
  consumer_info = DB.get_user_detail(cid, type)
  consumer_img_path = consumer_info['img_path']
  product_info = DB.get_product_detail(pid)
  product_img_path = product_info["product_img_path"]
  if consumer_img_path == "No_img":
    flash("해당 서비스 이용을 위해서는 사진 업로드가 필요합니다") 
    return redirect(url_for("upload_img", cid=cid))
  return render_template("try_on.html", consumer_img_path=consumer_img_path, product_img_path=product_img_path)

@app.route("/upload_img/<string:cid>")        # 회원가입때 이미지를 업로드하지 않은 경우
def upload_img(cid):
  return render_template("upload_img.html", cid=cid)

@app.route("/upload_done/<string:cid>", methods=["post"])
def upload_done(cid):
  img = None
  if 'consumer_img' in request.files:
    img = request.files['consumer_img']
  if DB.upload_img(img, cid): 
    return redirect(url_for("index"))
  else:
    flash("업로드에 실패했습니다")                  # 이미지를 업로드 하지 않은 채 제출한 경우
    return redirect(url_for("upload_img", cid=cid))
# =====================



# ======= 디자이너 제품 업로드 페이지 ========
@app.route("/upload_product")
def upload_product():
  did = request.args.get("did")
  print(did)
  return render_template("upload_product.html", did=did)

@app.route("/upload_product_done/<string:did>", methods=["post"])
def upload_product_done(did):
  product_img = request.files['product_img']
  product_info = {
    "product_name" : request.form.get("name"),
    "product_explain" : request.form.get("product_explain")
  }
  if DB.upload_product(product_img, product_info, did): 
    return redirect(url_for("index"))
  else:
    flash("제품명이 중복되거나 이미지가 업로드되지 않았습니다")                 
    return redirect(url_for("upload_product", did=did))
# ==========================================



# ====== 관리 페이지 =======
@app.route("/user_manage")       
def user_manage():
  if "id" not in session or session["id"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 유저 관리 가능
    return redirect(url_for("index"))
  consumers = DB.get_users("consumer")
  designers = DB.get_users("designer")
  return render_template("user_manage.html", consumers=consumers, designers=designers)

@app.route("/product_manage")       
def product_manage():
  if "id" not in session or session["id"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 유저 관리 가능
    return redirect(url_for("index"))
  products = DB.get_products()
  return render_template("product_manage.html", products = products)
# =========================



# ======= 관리(삭제) 페이지 ========
@app.route("/user_delete")       
def user_delete():
  type = request.args.get('type')
  uid = request.args.get('uid')
  if "id" not in session or session["id"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 유저 삭제 가능
    return redirect(url_for("index"))
  DB.user_delete(type, uid)
  return redirect(url_for("user_manage"))

@app.route("/product_delete")       
def product_delete():
  pid = request.args.get("pid")
  if "id" not in session or session["id"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 제품 삭제 가능
    return redirect(url_for("index"))
  DB.product_delete(pid)
  return redirect(url_for("product_manage"))
# ================================



# ===== 서버 실행 =====
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True)


