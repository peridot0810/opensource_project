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



  # ======= 회원가입 =======
  def signin_verification(self, id, type):         # 회원가입 검증
    id_list = self.get_users(type)
    try:
      for i in id_list:
        if id == i:                                # 중복 ID가 있다면 False 반환
          return False
      return True
    except:                                        # except : 회원이 한명도 없는 경우 (users가 None)
      return True

  def signin(self, id, pwd, name, img, type):
    information = {                           # consumer, designer 공통 정보
      "pwd" : pwd,
      "name" : name,
      "type" : type
    }

    try:                          
      if type == 'consumer':                  # 유저가 consumer -> 이미지, 이미지 경로 저장
        extension = img.filename.split(".")[1]
        img_name = f'{id}.{extension}'
        path = os.path.join('static/consumer_img', img_name)
        img.save(path)
        information["img_path"] = path

      elif type == 'designer':                # 유저가 designer -> 제품 등록용 폴더 생성, 폴더 경로 저장
        folder_name = id
        path = os.path.join('static/designer_products', folder_name)
        if not os.path.exists(path):          
          os.makedirs(path)  

    except:                                   # consumer유저가 이미지 등록 안한 경우 
      information["img_path"] = "No_img"

    if self.signin_verification(id, type):
      self.db.child(f"{type}s").child(id).set(information)
      return True
    else:
      return False
  # =========================



  # ===== 로그인 ======
  def login(self, id, pwd, type):
    userinfo = self.get_user_detail(id, type)
    try:
      if pwd == userinfo["pwd"]:
        return True
      else:
        return False
    except:                                         # except : 회원이 한명도 없는 경우 (userinfo가 None)
      return False
  # =================


  
  # ===== 제품 등록 =====
  def registration_verification(self, pid):          # 제품 등록 검증 (pid(product id)가 겹치는 경우는 없는지 확인)
    products = self.get_products()
    try:
      for i in products:
        if pid == i:
          return False
      return True
    except:                                          # except : 제품이 하나도 없는 경우 (products가 None)
      return True

  def product_registration(self, pid, price, product_name, product_explain, product_img):
    try:
      extension = product_img.filename.split(".")[1]
      product_id_ext = f"{pid}.{extension}"
      path = os.path.join(f'static/product_img', product_id_ext)
      product_img.save(path)
      print("저장 성공")
    except:
      return False

    information = {
      "price" : price,
      "product_name" : product_name,
      "product_explain" : product_explain,
      "product_img_path" : path
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


  # ===== 디자이너 제품 정보 가져오기 =====
  def get_designer_products(self, did):                 # 모든 제품 목록 가져오기
    try:
      products = self.db.child("designers").child(did).child("products").get().val()
      return products
    except:
      return None

  def get_designer_products_detail(self, did, product_name):      # 개별 제품의 세부정보 가져오기
    try:
      product_info = self.get_designer_products(did)[product_name]
      return product_info
    except:
      return None
  # ===========================


  # ====== 유저 정보 가져오기 =====
  def get_users(self, type):                    # 해당 타입의 유저 목록 가져오기
    try:
      users = self.db.child(f"{type}s").get().val()
      return users
    except:
      return None
  
  def get_user_detail(self, uid, type):         # 개별 유저 세부정보 가져오기
    try:
      user_info = self.get_users(type)[uid]
      return user_info
    except:
      return None
  # =============================



  # ======= 이미지 업로드 =======
  def upload_img(self, img, cid):
    try:
      extension = img.filename.split(".")[1]
      img_name = f'{cid}.{extension}'
      path = os.path.join('static/consumer_img', img_name)
      img.save(path)
    except:
      return False
    update_info = {
      "img_path" : path,
    }
    self.db.child("consumers").child(cid).update(update_info)
    return True
  # =============================


  # ========= 디자이너 제품 업로드 ============
  def designer_registration_verification(self, did, product_name):          # 제품 등록 검증 (pid(product id)가 겹치는 경우는 없는지 확인)
    products = self.get_designer_products(did)
    try:
      for i in products:
        if product_name == i:
          return False
      return True
    except:                                          # except : 제품이 하나도 없는 경우 (products가 None)
      return True

  def upload_product(self, product_img, product_info, did):
    try:
      extension = product_img.filename.split(".")[1]
      product_name = f"{product_info['product_name']}.{extension}"
      path = os.path.join(f'static/designer_products/{did}', product_name)
      product_img.save(path)
      print("저장 성공")
    except:
      return False
    
    if self.designer_registration_verification(did, product_name):
      product_info["designer_product_path"] = path
      self.db.child("designers").child(did).child("products").child(product_info['product_name']).set(product_info)
      return True
    else:
      return False
  # ======================================




  # ====== 유저/제품 삭제 ======
  def user_delete(self, type, uid):
    user_info = self.get_user_detail(uid, type)
    if type == "consumer":
      if user_info["img_path"] != "No_img":
        os.remove(user_info["img_path"])

    elif type == "designer":
      if os.path.exists(f"static/designer_products/{uid}"):
        shutil.rmtree(f"static/designer_products/{uid}")  

    self.db.child(f"{type}s/{uid}").remove()
    return True
  
  def product_delete(self, pid):
    product_info = self.get_product_detail(pid)
    img_path = product_info["product_img_path"]
    self.db.child(f"products/{pid}").remove()
    if os.path.exists(img_path):
      os.remove(img_path)

    return True
  # =========================