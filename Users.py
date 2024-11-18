
class User :
  def __init__(self, id, pwd, name, phone, email, type):
    self.id = id
    self.pwd = pwd
    self.type = type
    self.name = name
    self.phone = phone
    self.email = email


class Consumer(User):
  def __init__(self, cid : str, pwd : str, name : str, phone : str, email : str):
    super().__init__(cid, pwd, name, phone, email, "Consumer")
    self.img_path = None


class Designer(User):
  def __init__(self, did : str, pwd : str, name : str, phone : str, email : str):
    super().__init__(did, pwd, name, phone, email, "Designer")
    self.dir_path = f"static/designer_products/{did}"
    self.products = {}


class Root(User):
  def __init__(self, rid : str, pwd : str, name : str):
    super().__init__(rid, pwd, name, None, None, "Root")

