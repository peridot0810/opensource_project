from DB import DBModule
from flask import Flask, redirect, render_template, url_for, request, flash, session
from Users import Consumer, Designer, Root


class Server:
  def __init__(self):
    self.db = DBModule()
    self.User = None
    

  # ======== 회원가입 ==========
  def sign_in(self, user_info : dict, img):
    if self.db.sign_in(user_info, img):
      return True
    else:
      return False
  # ============================
  


  # ========= 로그인/로그아웃 ============
  def log_in(self, login_info : dict):
    User_info = self.db.log_in(login_info)  # User 정보를 dict 형태로 반환
    if User_info:    # 로그인 성공
      self.make_User(User_info)
      # 세션 열기
      session["id"] = User_info["id"]
      session["type"] = User_info["type"]
      return True
    else:                             # 로그인 실패
      return False
    
  def log_out(self):
    self.User = None
    session.pop("id")
    session.pop("type")
    return True
  # ==================================




  # ============= 로그인 여부 체크 =============
  def check_login(self):
    if "id" in session:                # 로그인이 되어있다면  -> user = 유저 아이디, user_type = 사용자 타입
      return self.User
    else:                              # 로그인되어있지 않다면 -> None
      raise Exception("로그인 상태가 아닙니다")
  # ========================================
    


  # ========= 제품 등록 ===============
  def product_registration(self, product_info, product_img, type, did=None, category=None):
    if self.db.product_registration(product_info, product_img, type, did, category):
      if type == "Designer":
        self.User.products[product_info["pid"]] = product_info
        print(self.User.products)
      return True
    else:
      return False
  # ========================================



  # =============== 제품 get ================
  def get_products(self, category=None):
    try:
      user_type = self.User.type
    except:
      user_type = None

    if user_type == "Designer":
      products = self.db.get_products(did = self.User.id)
    elif category != None:  # 특정 카테고리의 제품만 가져오기
      products = self.db.get_products(category=category)
    else:                   # 모든 제품 가져오기
      products = self.db.get_products()
    return products
  
  def get_product_detail(self, pid, did=None, category=None):
    product_detail = self.db.get_product_detail(pid, did = did, category=category)
    return product_detail
  
  # Consumer를 위한 함수 -> Designer는 사용 안하는 것으로 생각
  def get_products_by(self, by, category=None, num=None, sort=None):
    products = self.db.get_products_by(by, category=category, num=num, sort=sort)
    return products
  # ========================================




  # =============== 사용자 get ===============
  def get_users(self, type):
    users = self.db.get_users(type)
    if users:
      return users
    else:
      return None

  def get_user_detail(self, id, type):
    user = self.db.get_user_detail(id, type)
    if user:
      return user
    else:
      return None
  # =========================================




  # ========== 유저/제품 삭제 =========
  def user_delete(self, type, id):
    return self.db.user_delete(type, id)
    
  def product_delete(self, type, pid, did=None, category=None):
    print(category)
    if self.db.product_delete(type, pid, did=did, category=category):
      if type == "Designer":
        del self.User.products[pid]
        print(self.User.products)
      return True
    else:
      return False

  # ================================




  # ========== 유저 정보 수정 ==========
  def edit_info(self, id, type, update_info):
    new_user_info = self.db.edit_info(id, type, update_info)
    if new_user_info:
      print(new_user_info)
      self.log_out()
      self.log_in(new_user_info)
      # self.User 업데이트
      self.User.pwd = new_user_info["pwd"]
      return True
    else:
      return False
    
  def upload_img(self, img, cid):
    img_path = self.db.upload_img(img, cid)
    if img_path:
      self.User.img_path = img_path
      return True
    else:
      return False
  # ==================================




  # =========== 기타 함수 ==============
  def make_User(self, User_info):
    type = User_info["type"]
    if type == "Consumer":
      self.User = Consumer(User_info["id"], User_info["pwd"], User_info["name"], User_info["phone"], User_info["email"])
      self.User.img_path = self.get_user_detail(User_info["id"], "Consumer")["img_path"]
      print(self.User.img_path)
    elif type == "Designer":
      self.User = Designer(User_info["id"], User_info["pwd"], User_info["name"], User_info["phone"], User_info["email"])
      products = self.get_products()
      if products:
        self.User.products = products
      print(self.User.products)
    elif type == "Root":
      self.User = Root(User_info["id"], User_info["pwd"], User_info["name"])
  # ===================================