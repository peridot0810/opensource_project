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
  def product_registration(self, product_info, product_img, type, did=None):
    return self.db.product_registration(product_info, product_img, type, did)
  # ========================================



  # =============== 제품 get ================
  def get_products(self):
    try:
      user_type = self.User.type
    except:
      user_type = None

    if user_type == "Designer":
      products = self.db.get_products(did = self.User.id)
    else:   # Consumer, Root, 로그인 X
      products = self.db.get_products()
    return products
  
  def get_product_detail(self, pid, did=None):
    product_detail = self.db.get_product_detail(pid, did = did)
    return product_detail
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
    
  def product_delete(self, type, pid, did=None):
    return self.db.product_delete(type, pid, did=did)

  # ================================




  # ========== 유저 정보 수정 ==========
  def edit_info(self, id, type, update_info):
    new_user_info = self.db.edit_info(id, type, update_info)
    print(new_user_info)
    if new_user_info:
      self.log_out()
      self.log_in(new_user_info)
      return True
    else:
      return False
  # ==================================




  # =========== 기타 함수 ==============
  def make_User(self, User_info):
    type = User_info["type"]
    if type == "Consumer":
      self.User = Consumer(User_info["id"], User_info["pwd"], User_info["name"])
    elif type == "Designer":
      self.User = Designer(User_info["id"], User_info["pwd"], User_info["name"])
    elif type == "Root":
      self.User = Root(User_info["id"], User_info["pwd"], User_info["name"])
  # ===================================