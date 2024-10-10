import pyrebase
import json
import uuid  

class DBModule:  
  def __init__(self):
    with open("./auth/firebaseAuth.json") as f:
      config = json.load(f)
    
    firebase = pyrebase.initialize_app(config)   # 데이터베이스 앱 초기화
    self.db = firebase.database()                # 데이터베이스 연결

  def signin_verification(self, uid):
    users = self.db.child("users").get().val()
    try:
      for i in users:
        if uid == i:
          return False
      return True
    except:
      return True

  def signin(self, uid, pwd, name):
    information = {
      "pwd" : pwd,
      "name" : name
    }
    if self.signin_verification(uid):
      self.db.child("users").child(uid).set(information)
      return True
    else:
      return False
    
  def login(self, uid, pwd):
    users = self.db.child("users").get().val()
    try:
      userinfo = users[uid]
      if pwd == userinfo["pwd"]:
        return True
      else:
        return False
    except:
      return False
      
