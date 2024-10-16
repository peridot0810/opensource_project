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
  if "uid" in session:               # 로그인이 되어있다면  -> user = 유저 아이디
    user = session['uid']
  else:                              # 로그인되어있지 않다면 -> user = "Login_needed"
    user = "Login_needed"

  products = DB.get_products()
  if not products:                   # product가 없음 -> 제품 가져오기 실패
    return render_template("index.html", user = user, products = "No_products")
  return render_template("index.html", user = user, products = products)  # index.html에 user, products 넘기기
# =====================



# ===== 회원가입 =====
@app.route("/signin") 
def signin():
  if "uid" in session:               # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  return render_template("signin.html")

@app.route("/signin_done", methods=["post"])  
def signin_done():
  uid = request.form.get("id")
  pwd = request.form.get("pwd")
  name = request.form.get("name")
  img = None
  if 'user_img' in request.files:
    img = request.files['user_img']
  
  if DB.signin(uid, pwd, name, img):      # 회원가입 성공
    return redirect(url_for("login"))
  else:
    flash("이미 존재하는 아이디 입니다")         # 회원가입 실패
    return redirect(url_for("signin"))
# ======================



# ===== 로그인/로그아웃 =====
@app.route("/login") 
def login():
  if "uid" in session:                # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  return render_template("login.html")

@app.route("/login_done", methods=["post"])  
def login_done():
  uid = request.form.get("id")
  pwd = request.form.get("pwd")
  if DB.login(uid, pwd):              # 로그인 성공 -> session["uid"] = 유저 아이디
    session["uid"] = uid
    return redirect(url_for("index"))
  else:                               # 로그인 실패
    flash("아이디가 없거나 틀린 비밀번호 입니다")
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
  if "uid" in session:                # 로그인 상태라면 session에서 "uid"라는 key를 pop
    session.pop("uid")
    return redirect(url_for("index"))
  else:                               # 로그인 상태가 아니라면 redirect -> 로그인 창
    return redirect(url_for("login"))
# =================================
  


# ====== 제품 등록 ======
@app.route("/product_registration")  
def product_registration():
  if "uid" not in session or session["uid"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 제품 등록 가능 
    return redirect(url_for("index"))
  return render_template("product_registration.html")

@app.route("/registration_done", methods=["post"])  
def registration_done():
  pid = request.form.get("id")
  price = request.form.get("price")
  product_name = request.form.get("name")
  product_explain = request.form.get("product_explain")
  if DB.product_registration(pid, price, product_name, product_explain):  # 제품 등록 성공
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
  if "uid" not in session:
    flash("로그인이 필요한 서비스입니다") 
    return redirect(url_for("login"))
  uid = session["uid"]
  user_info = DB.get_user_detail(uid)
  user_img_path = user_info['img_path']
  if user_img_path == "No_img":
    flash("해당 서비스 이용을 위해서는 사진 업로드가 필요합니다") 
    return redirect(url_for("upload_img", uid=uid))
  return render_template("try_on.html", img_path=user_img_path, pid=pid)

@app.route("/upload_img/<string:uid>")        # 회원가입때 이미지를 업로드하지 않은 경우
def upload_img(uid):
  return render_template("upload_img.html", uid=uid)

@app.route("/upload_done/<string:uid>", methods=["post"])
def upload_done(uid):
  img = None
  if 'user_img' in request.files:
    img = request.files['user_img']
  if DB.upload_img(img, uid): 
    return redirect(url_for("index"))
  else:
    flash("업로드에 실패했습니다")                  # 이미지를 업로드 하지 않은 채 제출한 경우
    return redirect(url_for("upload_img", uid=uid))
# =====================



# ====== 관리 페이지 =======
@app.route("/user_manage")       
def user_manage():
  if "uid" not in session or session["uid"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 유저 관리 가능
    return redirect(url_for("index"))
  users = DB.get_users()
  return render_template("user_manage.html", users=users)

@app.route("/product_manage")       
def product_manage():
  if "uid" not in session or session["uid"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 유저 관리 가능
    return redirect(url_for("index"))
  products = DB.get_products()
  return render_template("product_manage.html", products = products)
# =========================



# ======= 관리(삭제) 페이지 ========
@app.route("/user_delete/<string:uid>")       
def user_delete(uid):
  if "uid" not in session or session["uid"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 유저 삭제 가능
    return redirect(url_for("index"))
  DB.user_delete(uid)
  return redirect(url_for("user_manage"))

@app.route("/product_delete/<string:pid>")       
def product_delete(pid):
  if "uid" not in session or session["uid"] != "root":   # 로그인 되어있고, 유저 아이디가 "root"일때만 제품 삭제 가능
    return redirect(url_for("index"))
  DB.product_delete(pid)
  return redirect(url_for("product_manage"))
# ================================



# ===== 서버 실행 =====
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True)


