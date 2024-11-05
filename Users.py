
class User :
  def __init__(self, id : str, pwd : str, name : str, type : str):
    self.id = id
    self.pwd = pwd
    self.type = type
    self.name = name


class Consumer(User):
  def __init__(self, cid : str, pwd : str, name : str):
    super().__init__(cid, pwd, name, "Consumer")
    self.img_path = None


class Designer(User):
  def __init__(self, did : str, pwd : str, name : str):
    super().__init__(did, pwd, name, "Designer")
    self.dir_path = f"static/designer_products/{did}"
    self.products = {}


class Root(User):
  def __init__(self, rid : str, pwd : str):
    super().__init__(rid, pwd, "Root", "Root")

