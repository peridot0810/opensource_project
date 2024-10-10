from flask import Flask, redirect, render_template, url_for, request, flash, session
from DB_handler import DBModule

app = Flask(__name__)
app.secret_key = "as;dlkjgao;psjr"   # 아무거나 친거. 유출되면 안되는 키
DB = DBModule()  # 데이터베이스 객체

@app.route("/")  # 홈페이지
def index():
  if "uid" in session:
    user = session['uid']
  else:
    user = "Login_needed"
  return render_template("index.html", user = user)


@app.route("/signin") # 회원가입창
def signin():
  if "uid" in session:
    return redirect(url_for("index"))
  return render_template("signin.html")

@app.route("/signin_done", methods=["get"])  
def signin_done():
  uid = request.args.get("id")
  pwd = request.args.get("pwd")
  name = request.args.get("name")
  
  if DB.signin(uid, pwd, name):  # 회원가입 성공
    return redirect(url_for("index"))
  else:
    flash("이미 존재하는 아이디 입니다")
    return redirect(url_for("signin"))


@app.route("/login")  # 로그인창
def login():
  if "uid" in session:
    return redirect(url_for("index"))
  return render_template("login.html")

@app.route("/login_done", methods=["get"])  
def login_done():
  uid = request.args.get("id")
  pwd = request.args.get("pwd")
  if DB.login(uid, pwd):
    session["uid"] = uid
    return redirect(url_for("index"))
  else:
    flash("아이디가 없거나 틀린 비밀번호 입니다")
    return redirect(url_for("login"))
  
@app.route("/logout")
def logout():
  if "uid" in session:
    session.pop("uid")
    return redirect(url_for("index"))
  else:
    return redirect(url_for("login"))




if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True)
