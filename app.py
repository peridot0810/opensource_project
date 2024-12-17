from flask import Flask, redirect, render_template, url_for, request, flash, session
from flask_cors import CORS
from DB import DBModule
from Users import Consumer, Designer, Root
from Server import Server
from Products import Product
import os

# ==== 초기 설정 ====
app = Flask(__name__)
app.secret_key = os.urandom(24)      # 랜덤 secret key -> 서버 시작할때마다 세션 초기화
CORS(app)
Server = Server()                    # Server 인스턴스 생성
# =================
#======김동우 테스트용======

@app.route('/vton1')
def ren_vton1():
    """
    기본 경로로 접속하면 templates/index.html 파일을 렌더링합니다.
    """
    return render_template('vton1.html')
@app.route('/vton2')
def ren_vton2():
    """
    기본 경로로 접속하면 templates/index.html 파일을 렌더링합니다.
    """
    return render_template('vton2.html')
@app.route('/pd')
def ren_pd():
    """
    기본 경로로 접속하면 templates/index.html 파일을 렌더링합니다.
    """
    return render_template('product_detail.html')
@app.route('/ct')
def ren_ct():
    """
    기본 경로로 접속하면 templates/index.html 파일을 렌더링합니다.
    """
    return render_template('cart.html')
@app.route('/su')
def ren_su():
    """
    기본 경로로 접속하면 templates/index.html 파일을 렌더링합니다.
    """
    return render_template('signup.html')
@app.route('/vd')
def ren_vd():
    """
    기본 경로로 접속하면 templates/index.html 파일을 렌더링합니다.
    """
    return render_template('vton_design.html')
#=================


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

  if user_type != "Designer" :
    products = Server.get_products_by("sales_volume", num=4, sort="DESC")
  else:
    products = Server.get_products()

  if not products:                   # product가 없음 -> 제품 가져오기 실패
    products = "No_products"

  print(products)
  return render_template("index.html", user = user_id, type = user_type, products = products)  # index.html에 user, products 넘기기
# =====================



# =========== 제품 카테고리 페이지 ==========
@app.route('/category')
def category():
  try:
    user = Server.check_login()
    user_id = user.id
    user_type = user.type
  except:
    user_id = "Login_needed"
    user_type = None

  products = Server.get_products()
  print(products)
  if not products:                   # product가 없음 -> 제품 가져오기 실패
    products = "No_products"
  print(products)

  return render_template('category.html', products = products, user_type = user_type)
# ======================================



# ========= 마이 페이지 ===========
@app.route("/my_page")
def my_page():
  try:
    user = Server.check_login()
  except Exception as e:
    print(e)
    return redirect(url_for("login"))
  
  user_info = Server.get_user_detail(user.id, user.type)
  
  return render_template("mypage.html", user_info = user_info, user_type=user.type)
# ===============================



# ========= 내 정보 수정 ============
@app.route("/edit_done", methods=["post"])  
def edit_done():
  try:
    user = Server.check_login()
  except:
    return redirect(url_for("index"))
  
  update_info = {
    "current_pwd" : request.form.get("current_pwd"),
    "new_pwd" : request.form.get("new_pwd"),
    "confirm_pwd" : request.form.get("confirm_pwd"),
  }

  if Server.edit_info(user.id, user.type, update_info): # 정보 수정 성공
    flash("비밀번호 변경 완료")
    return redirect(url_for("my_page"))    
  else:
    flash("정보 수정 실패")                                # 정보 수정 실패
    return redirect(url_for("my_page"))
# ===============================



# ===== 회원가입 =====
@app.route("/signin_userType")
def signin_userType():                           # Designer, Consumer 구분
  try:
    Server.check_login()                  # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    return render_template("signin_userType.html")

@app.route("/signin") 
def signin():
  try:
    Server.check_login()                      # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    type = request.form.get("type")

    return render_template("signup.html")                                   

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
      "phone" : request.form.get("phone"),
      "email" : request.form.get("email"),
      "type" : request.form.get("type")
    }

    img = request.files.get('profile_image')

    if Server.sign_in(user_info, img):                 # 회원가입 성공
      return redirect(url_for("login"))    
    else:
      flash("이미 존재하는 아이디 입니다")                    # 회원가입 실패
      return redirect(url_for("signin"))

@app.route("/signin_Root") 
def signin_Root():
  try:
    Server.check_login()                      # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    pass
  return render_template("signin_root.html")   
# ======================



# ===== 로그인/로그아웃 =====
@app.route("/login") 
def login():
  try:
    Server.check_login()                # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    return render_template("login.html", type = request.form.get("type"))

@app.route("/login_Root") 
def login_Root():
  try:
    Server.check_login()                # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    return render_template("login.html", type = "Root")

@app.route("/login_done", methods=["post"])  
def login_done():
  try:
    Server.check_login()                     # 로그인 상태라면 redirect -> 메인페이지
    return redirect(url_for("index"))
  except:
    data = request.get_json()

    login_info = {
      "id" : data.get("id"),
      "pwd" : data.get("pwd"),
      "type" : data.get("type")
    }

    if Server.log_in(login_info):                  # 로그인 성공 -> session["id"] = 유저 아이디
      return redirect(url_for("index"))
    else:                                          # 로그인 실패
      flash("아이디가 없거나 틀린 비밀번호 입니다")
      return redirect(url_for("login"))

@app.route("/logout")
def logout():
  try:
    Server.check_login()                      
    Server.log_out()
    return redirect(url_for("index"))
  except:                                          # 로그인 상태가 아니라면 redirect -> 로그인 창
    return redirect(url_for("login"))
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
    "original_price" : request.form.get("original_price") ,
    "discounted_price" : request.form.get("discounted_price") ,
    "discount_rate" : request.form.get("discount_rate") ,
    "product_name" : request.form.get("name") ,
    "product_explain" : request.form.get("product_explain"),
    "rating" : request.form.get("rating"),
    "sales_volume" : request.form.get("sales_volume")  
  }
  product_img = request.files['product_img']

  if Server.product_registration(product_info, product_img, "Root", category=product_info["category"]):  # 제품 등록 성공
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
    "product_name" : request.form.get("product_name"),
    "product_explain" : request.form.get("product_explain")
  }
  print(product_info)

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

@app.route("/product_manage")   
def product_manage():
  try:
    user = Server.check_login()
    user_type = user.type
  except:                                              # 로그인 상태가 아닌 경우
    user_type = None

  if user_type == "Root":
    top = Server.get_products(category='top')
    pants = Server.get_products(category='pants')
    dress = Server.get_products(category='dress')
    outer = Server.get_products(category='outer')
    return render_template("product_manage.html", categories=[top, pants, dress, outer])
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
    flash("로그인이 필요한 서비스입니다") 
    return redirect(url_for("login"))
  
  if user.type == "Consumer" and user.img_path == "No_img":
    flash("해당 서비스 이용을 위해서는 사진 업로드가 필요합니다") 
    return redirect(url_for("my_page"))

  pid = request.args.get("pid")
  
  if user.type == "Consumer":
    product_info = Server.get_product_detail(pid)
    model_img_path = user.img_path
    render_html = "vton1.html"
  elif user.type == "Designer":
    product_info = Server.get_product_detail(pid, did=user.id)
    model_img_path = None
    render_html = "vton_design.html"
  product_img_path = product_info["img_path"]
  product_name = product_info["product_name"]
  
  return render_template(render_html, user_name = user.name, product_name = product_name, model_img_path=model_img_path, product_img_path=product_img_path, type=user.type, pid=pid)

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
    flash("이미지 업로드 성공")
    return redirect(url_for("my_page"))
  else:
    flash("업로드에 실패했습니다")                  # 이미지를 업로드 하지 않은 채 제출한 경우
    return redirect(url_for("my_page", cid=cid))
# ================================



# ========= header/footer 렌더링 ==========
@app.route('/header')
def header():
    try:
      user = Server.check_login()
      user_id = user.id
      user_type = user.type
    except:
      user_id = "Login_needed"
      user_type = None
    return render_template('components/header.html', user_id=user_id, user_type = user_type)  # templates/components/header.html 렌더링

@app.route('/footer')
def footer():
    return render_template('components/footer.html')  # templates/components/footer.html 렌더링
# ================================





# ===== 서버 실행 =====
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True, port=8080)