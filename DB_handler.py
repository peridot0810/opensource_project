import pyrebase
import json
import os

class DBModule:  
  def __init__(self):
    with open("./auth/firebaseAuth.json") as f:
      config = json.load(f)
    
    firebase = pyrebase.initialize_app(config)     # 데이터베이스 앱 초기화
    self.db = firebase.database()                  # 데이터베이스 연결

  # ======= 회원가입 =======
  def signin_verification(self, uid):              # 회원가입 검증
    users = self.get_users()
    try:
      for i in users:
        if uid == i:                               # 중복 ID가 있다면 False 반환
          return False
      return True
    except:                                        # except : 회원이 한명도 없는 경우 (users가 None)
      return True

  def signin(self, uid, pwd, name, img):
    try:                                           # 이미지 저장 및 파이어베이스에 업로드
      extension = img.filename.split(".")[1]
      img_name = f'{uid}.{extension}'
      img_path = os.path.join('static/user_img', img_name)
      img.save(img_path)
    except:
      img_path = "No_img"
    
    information = {
      "pwd" : pwd,
      "name" : name,
      "img_path": img_path,
    }
    if self.signin_verification(uid):
      self.db.child("users").child(uid).set(information)
      return True
    else:
      return False
  # =========================



  # ===== 로그인 ======
  def login(self, uid, pwd):
    userinfo = self.get_user_detail(uid)            # userinfo : 딕셔너리
    try:
      if pwd == userinfo["pwd"]:
        return True
      else:
        return False
    except:                                         # except : 회원이 한명도 없는 경우 (userinfo가 None)
      return False
  # =================


  
  # ===== 제품 등록 =====
  def registration_verification(self, pid):          # 제품 등록 검증 (pid : product id가 겹치는 경우는 없는지 확인)
    products = self.get_products()
    try:
      for i in products:
        if pid == i:
          return False
      return True
    except:                                          # except : 제품이 하나도 없는 경우 (products가 None)
      return True

  def product_registration(self, pid, price, product_name, product_explain):
    information = {
      "price" : price,
      "product_name" : product_name,
      "product_explain" : product_explain
    }
    if self.registration_verification(pid):
      self.db.child("products").child(pid).set(information)
      return True
    else:
      return False
  # ==================


  # ===== 제품 정보 가져오기 =====
  def get_products(self):                 # 모든 제품 목록 가져오기
    try:
      products = self.db.child("products").get().val()
      return products
    except:
      return None

  def get_product_detail(self, pid):      # 개별 제품의 세부정보 가져오기
    try:
      product_info = self.get_products()[pid]
      return product_info
    except:
      return None
  # ===========================


  # ====== 유저 정보 가져오기 =====
  def get_users(self):                    # 모든 유저 목록 가져오기
    try:
      users = self.db.child("users").get().val()
      return users
    except:
      return None
  
  def get_user_detail(self, uid):         # 개별 유저의 세부정보 가져오기
    try:
      user_info = self.get_users()[uid]
      return user_info
    except:
      return None
  # =============================



  # ======= 이미지 업로드 =======
  def upload_img(self, img, uid):
    try:
      extension = img.filename.split(".")[1]
      img_name = f'{uid}.{extension}'
      img_path = os.path.join('static/user_img', img_name)
      img.save(img_path)
    except:
      return False
    update_info = {
      "img_path" : img_path,
    }
    self.db.child("users").child(uid).update(update_info)
    return True
  # =============================


  # ====== 유저/제품 삭제 ======
  def user_delete(self, uid):
    user_info = self.get_user_detail(uid)
    if user_info["img_path"] != "No_img":
      os.remove(user_info["img_path"])
    self.db.child(f"users/{uid}").remove()
    return True
  
  def product_delete(self, pid):
    self.db.child(f"products/{pid}").remove()
    return True
  # =========================