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
      if User_info["type"] == "Consumer":
        self.User = Consumer(User_info["id"], User_info["pwd"], User_info["name"])
      elif User_info["type"] == "Designer":
        self.User = Designer(User_info["id"], User_info["pwd"], User_info["name"])
      elif User_info["type"] == "Root":
        self.User = Root(User_info["id"], User_info["pwd"], User_info["name"])
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
      user = self.User.id
      user_type = self.User.type
      return user, user_type
    else:                              # 로그인되어있지 않다면 -> None
      return None
  # ========================================
    

  # =============== 제품 get ================
  def get_products(self):
    try:
      if self.User.type == "Designer":
        products = self.db.get_designer_products(self.User.id)
      else:   # Consumer, Root
        products = self.db.get_products()
    except:   # 로그인 X
      return None
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
    if self.db.user_delete(type, id):
      return True
    else:
      return False


  # ================================

  # ========== 유저 정보 수정 ==========
  def edit_info(self, id, type, update_info):
    new_user_info = self.db.edit_info(id, type, update_info)
    if new_user_info:
      print("서버 : 수정 성공")
      self.log_out()
      self.log_in(new_user_info)
      return True
    else:
      print("서버 : 수정 실패")
      return False
  # ==================================