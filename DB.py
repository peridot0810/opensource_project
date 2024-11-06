import pyrebase
import json
import os
import shutil


class DBModule:
  def __init__(self):
    with open("./auth/firebaseAuth.json") as f:
      config = json.load(f)
    
    firebase = pyrebase.initialize_app(config)     # 데이터베이스 앱 초기화
    self.db = firebase.database()                  # 데이터베이스 연결


  # ====== 회원 가입 ========
  def signin_verification(self, id, type):         # 회원가입 검증
    id_list = self.get_users(type)
    try:
      for i in id_list:
        if id == i:                                # 중복 ID가 있다면 False 반환
          return False
      return True
    except:                                        # except : 회원이 한명도 없는 경우 (users가 None)
      return True


  def sign_in(self, user_info : dict, img):
    id = user_info["id"]
    type = user_info["type"]
    if type == 'Consumer':                   # 유저가 consumer -> 이미지, 이미지 경로 저장
      try:                              
        extension = img.filename.split(".")[1]
        img_name = f'{id}.{extension}'
        path = os.path.join('static/consumer_img', img_name)
        img.save(path)
        user_info["img_path"] = path
      except:
        user_info["img_path"] = "No_img"

    elif type == 'Designer':                 # 유저가 designer -> 제품 등록용 폴더 생성, 폴더 경로 저장
      folder_name = id
      path = os.path.join('static/designer_products', folder_name)
      if not os.path.exists(path):          
        os.makedirs(path)  

    elif type == 'Root':
      pass

    if self.signin_verification(id, type):
      self.db.child(f"{type}s/{id}").set(user_info)
      return True
    else:
      return False
    
  # ================================================


  # =========== 로그인 ===============
  def log_in(self, login_info : dict):
    User_info = self.get_user_detail(login_info["id"], login_info["type"])
    if User_info and login_info["pwd"] == User_info["pwd"]:   # 해당하는 유저 존재함 + 로그인 성공
      return User_info
    else:
      return False
  # ===================================


  # ======== 유저 정보 가져오기 ========
  def get_users(self, type):                    # 해당 타입의 유저 목록 가져오기
    try:
      users = self.db.child(f"{type}s").get().val()
      return users
    except:
      return None
  
  def get_user_detail(self, id, type):         # 개별 유저 세부정보 가져오기
    try:
      user_info = self.get_users(type)[id]
      return user_info
    except:
      return None
  # ====================================
    
      

  # ========== 제품 정보 가져오기 ===========
  def get_designer_products(self, did):
    try:
      products = self.db.child(f"designers/{did}/products").get().val()
      return products
    except:
      return None

  def get_products(self):
    try:
      products = self.db.child("products").get().val()
      return products
    except:
      return None
  # ========================================


  # ============= 유저/제품 삭제 ===============
  def user_delete(self, type, id):
    print("삭제 시도 - DB")
    print(f"삭제 타입 : {type}")
    try:
      user_info = self.get_user_detail(id, type)
      if type == "Consumer":
        if user_info["img_path"] != "No_img":
          os.remove(user_info["img_path"])

      elif type == "Designer":
        if os.path.exists(f"static/designer_products/{id}"):
          shutil.rmtree(f"static/designer_products/{id}")  

      elif type == "Root":
        pass

      self.db.child(f"{type}s/{id}").remove()
      print("삭제 성공 - DB")
      return True
    except:
      return False

  # ========================================