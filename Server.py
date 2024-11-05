from DB import DBModule
from flask import Flask, redirect, render_template, url_for, request, flash, session
from Users import Consumer, Designer, Root


class Server:
  def __init__(self):
    self.db = DBModule()
    self.User = None
    

  def sign_in(self, user_info : dict, img):
    if self.db.sign_in(user_info, img):
      return True
    else:
      return False
  

  def log_in(self, login_info : dict):
    User_info = self.db.log_in(login_info)  # User 정보를 dict 형태로 반환
    if User_info:    # 로그인 성공
      if User_info["type"] == "Consumer":
        self.User = Consumer(User_info["id"], User_info["pwd"], User_info["name"])
      elif User_info["type"] == "Designer":
        self.User = Designer(User_info["id"], User_info["pwd"], User_info["name"])
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


  def check_login(self):
    if "id" in session:                # 로그인이 되어있다면  -> user = 유저 아이디
      user = self.User.id
      user_type = self.User.type
      return user, user_type
    else:                              # 로그인되어있지 않다면 -> None
      return None

    

  def get_products(self):
    try:
      if self.User.type == "Designer":
        products = self.db.get_designer_products(self.User.id)
      else:   # Consumer, Root
        products = self.db.get_products()
    except:   # 로그인 X
      return None

  def get_users(self, type):
    pass

  def get_user_detail(self, id, type):
    pass