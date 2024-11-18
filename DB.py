import pyrebase
import json
import os
import shutil
import random


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
    


  # ============= 제품 등록  ==============  
  def product_registration(self, product_info, product_img, type, did=None, category=None):  # Root 제품 등록일때 did == None
    if type == "Designer":
        product_info["pid"] = f"{random.randint(100, 999)}"        # Designer 제품에도 pid 부여 : {랜덤3자리수}

    if self.registration_verification(product_info["pid"], type, did, category):
      try:
        extension = self.get_img_extension(product_img)
        path = self.set_img_path(product_info["pid"], extension, type, did=did, category=category)
        product_img.save(path)
        product_info["img_path"] = path
      except:
        product_info["img_path"] = "No_img"
  
      if type == "Root":
        self.db.child(f"Products/{product_info["pid"]}").set(product_info)
      elif type == "Designer":
        self.db.child(f"Designers/{did}/products/{product_info["pid"]}").set(product_info)

      return True
    else:
      if type == "Designer":                                            # Designer인데 제품 등록 검증 실패 -> 새로운 pid 부여 후 다시 시도
        return self.product_registration(product_info, product_img, type, did)
      else:
        return False
  # =======================================




  # ========== 제품 정보 가져오기 ===========
  def get_products(self, did=None, category=None):
    try:
      if did != None:
        products = self.db.child(f"Designers/{did}/products").get().val()
      elif category != None:
        print(category)
        products = self.db.child(f"Products/").order_by_child("category").equal_to(category).get().val()
        print(products)

      else :
        products = self.db.child(f"Products/").get().val()
      return products
    except Exception as e:
      print(e)
      return None
    
  def get_product_detail(self, pid, did=None, category=None):  # Designer가 호출한게 아니면 did == None
    try:
      product_info = self.get_products(did=did, category=category)[pid]
      return product_info
    except Exception as e:
      print(e)
      return None
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
    
  def product_delete(self, type, pid, did=None, category=None):
    try:
      product_info = self.get_product_detail(pid, did=did, category=category)
      self.delete_product_data(product_info, did=did)
      if type == "Root" :
        self.db.child(f"Products/{pid}").remove()
      elif type == "Designer" and did != None:
        self.db.child(f"Designers/{did}/products/{pid}").remove()
      return True
    except Exception as e:
      print(e)
      return False
  # ========================================


  # ========== 유저 정보 수정 ==========
  def edit_info(self, id, type, update_info):
    if id != update_info["id"] and not self.signin_verification(update_info["id"], type):
      return None

    try:
      if id != update_info["id"]:     # id를 변경한 경우
        if type == "Designer":
          products = self.get_products(did=id)
          if products:
            for product_id in products:
              parts = products[product_id]['img_path'].split('/')
              parts[-2] = update_info["id"]
              new_product_path = '/'.join(parts)
              self.db.child(f"{type}s/{id}/products/{product_id}/").update({"img_path" : new_product_path})

        user_info = self.get_user_detail(id, type)
        new_path = self.edit_user_data(id, user_info, update_info)
        user_info["img_path"] = new_path
        user_info["id"] = update_info["id"]
        user_info["pwd"] = update_info["pwd"]
        user_info["name"] = update_info["name"]

        self.db.child(f"{type}s/{update_info["id"]}").set(user_info)
        self.db.child(f"{type}s/{id}").remove()

      else:                           # id를 변경하지 않은 경우
        user_info = self.get_user_detail(id, type)
        user_info["pwd"] = update_info["pwd"]
        user_info["name"] = update_info["name"]

        self.db.child(f"{type}s/{id}").update(user_info)

      return user_info
    
    except Exception as e:
      print(e)
      return None
  
  def upload_img(self, img, cid):
    try:
      extension = self.get_img_extension(img)
      img_path = self.set_img_path(cid, extension, "Consumer")
      if os.path.exists(img_path):
        os.remove(img_path)
      img.save(img_path)
    except:
      return False
    
    update_info = {"img_path" : img_path}
    self.db.child(f"Consumers/{cid}").update(update_info)
    return img_path
  # ==================================





  # ========= 기타 함수 =============
  def get_img_extension(self, img):
    return img.filename.split(".")[1]
  
  def set_img_path(self, id, extension, type, did=None, category=None):
    img_name = f'{id}.{extension}'

    if type == "Consumer":
      path = os.path.join('static/consumer_img', img_name)
    elif type == "Root":
      path = os.path.join(f'static/product_img/{category}', img_name)
    elif type == "Designer":
      path = os.path.join(f'static/designer_products/{did}', img_name)

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

  def delete_product_data(self, product_info, did=None):
    if product_info["img_path"] != "No_img":
      os.remove(product_info["img_path"])

  def edit_user_data(self, id, user_info, update_info):
    if user_info["type"] == "Consumer" and user_info["img_path"]!="No_img":
      old_path = user_info["img_path"]
      extension = user_info["img_path"].split("/")[-1].split(".")[-1]
      new_path = f"static/consumer_img/{update_info["id"]}.{extension}"
    elif user_info["type"] == "Designer":
      old_path = f"static/designer_products/{id}" 
      new_path = f"static/designer_products/{update_info['id']}"

    try:
      os.rename(old_path, new_path)
      return new_path
    except Exception as e :
      print(e)
      return "No_img"
    
  def registration_verification(self, pid, type, did=None, category=None):    # 제품 등록 검증 (pid(product id)가 겹치는 경우는 없는지 확인)
    if type == "Root":
      products = self.get_products(category=category)
    elif type == "Designer" and did != None:
      products = self.get_products(did=did)
    else:
      products = None

    try:
      for i in products:
        if pid == i:
          return False
      return True
    except:                                                     # except : 제품이 하나도 없는 경우 (products가 None)
      return True
  # ================================