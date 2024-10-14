import pyrebase
import json
import os

class DBModule:  
  def __init__(self):
    with open("./auth/firebaseAuth.json") as f:
      config = json.load(f)
    
    firebase = pyrebase.initialize_app(config)     # 데이터베이스 앱 초기화
    self.db = firebase.database()                  # 데이터베이스 연결
    self.storage = firebase.storage()              # firebase 저장소 연결

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
    try:
      img_name = img.filename
      img_path = os.path.join('uploads', img_name)
      img.save(img_path)
      self.storage.child(img_name).put(img_path)
      img_url = self.storage.child(img_name).get_url(None)
    except:
      img_url = "No_img"
    
    information = {
      "pwd" : pwd,
      "name" : name,
      "img_url": img_url
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

  def product_registration(self, pid, price, product_name):
    information = {
      "price" : price,
      "product_name" : product_name
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
      img_name = img.filename
      img_path = os.path.join('uploads', img_name)
      img.save(img_path)
      self.storage.child(img_name).put(img_path)
      img_url = self.storage.child(img_name).get_url(None)
    except:
      return False
    user_info = self.get_user_detail(uid)
    user_info["img_url"] = img_url
    self.db.child("users").child(uid).set(user_info)
    return True
  # =============================