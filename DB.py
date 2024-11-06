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
    if id_list:
      for i in id_list:
        if id == i:                                # 중복 ID가 있다면 False 반환
          return False
      return True
    else:                                          # 회원이 한명도 없는 경우 (users가 None)
      return True

  def sign_in(self, user_info : dict, img):
    id = user_info["id"]
    type = user_info["type"]

    if not self.signin_verification(id, type):
      return False
    
    if type == 'Consumer':                   # 유저가 consumer -> 이미지, 이미지 경로 저장
      try:                              
        extension = self.get_img_extension(img)
        path = self.set_img_path(id, extension, type)
        img.save(path)
        user_info["img_path"] = path
      except:
        user_info["img_path"] = "No_img"

    elif type == 'Designer':                 # 유저가 designer -> 제품 등록용 폴더 생성, 폴더 경로 저장
      folder_name = id
      self.make_folder(folder_name, type)

    elif type == 'Root':
      pass

    self.db.child(f"{type}s/{id}").set(user_info)
    return True
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
  
  def get_user_detail(self, id, type):          # 개별 유저 세부정보 가져오기
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
    
  def get_product_detail(self):
    pass
  # ========================================


  # ============= 유저/제품 삭제 ===============
  def user_delete(self, type, id):
    try:
      user_info = self.get_user_detail(id, type)
      self.delete_user_data(user_info, type)
      self.db.child(f"{type}s/{id}").remove()
      return True
    except:
      return False
  # ========================================


  # ========== 유저 정보 수정 ==========
  def edit_info(self, id, type, update_info):
    if not self.signin_verification(update_info["id"], type):
      return None

    try:
      user_info = self.get_user_detail(id, type)
      print("DB : 수정 시도")
      new_path = self.edit_user_data(id, user_info, update_info)
      if not new_path:
        return None
      
      user_info["id"] = update_info["id"]
      user_info["pwd"] = update_info["pwd"]
      user_info["name"] = update_info["name"]
      user_info["img_path"] = new_path
      
      self.db.child(f"{type}s/{update_info["id"]}").set(user_info)
      self.db.child(f"{type}s/{id}").remove()
      return user_info
    
    except Exception as e:
      print(e)
      return None
  # ==================================





  # ========= 기타 함수 =============
  def get_img_extension(self, img):
    return img.filename.split(".")[1]
  
  def set_img_path(self, id, extension, type):
    if type == "Consumer":
      img_name = f'{id}.{extension}'
      path = os.path.join('static/consumer_img', img_name)
    if type == "Designer":
      path = None

    return path
  
  def make_folder(self, folder_name, type):
    if type == "Designer":
      path = os.path.join('static/designer_products', folder_name)
      if not os.path.exists(path):          
        os.makedirs(path)  
    if type == "Consumer":
      path = None

    return path

  def delete_user_data(self, user_info, type):
    if type == "Consumer":
        if user_info["img_path"] != "No_img":
          os.remove(user_info["img_path"])

    elif type == "Designer":
      if os.path.exists(f"static/designer_products/{user_info["id"]}"):
        shutil.rmtree(f"static/designer_products/{user_info["id"]}")  

    elif type == "Root":
      pass

  def edit_user_data(self, id, user_info, update_info):
    print("DB : 수정 시작")
    if user_info["type"] == "Consumer" and user_info["img_path"]!="No_img":
      old_path = user_info["img_path"]
      extension = user_info["img_path"].split("/")[-1].split(".")[-1]
      new_path = f"static/consumer_img/{update_info["id"]}.{extension}"
      print("DB : Consumer 수정 완료")
    elif user_info["type"] == "Designer":
      old_path = f"static/designer_products/{id}" 
      new_path = f"static/designer_products/{update_info['id']}"
      print("DB : Designer 수정 완료")

    try:
      os.rename(old_path, new_path)
      print("DB : rename까지 완료")
      return new_path
    except Exception as e :
      print(e)
      return None
    

  # ================================