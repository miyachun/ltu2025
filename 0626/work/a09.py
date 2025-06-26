from flask import Flask, redirect, url_for, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"

a= random.randint(1,10)
b= random.randint(1,10)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html",a=a,b=b)

@app.route("/user")
def user():
    if "user" in session:
        user = int(session["user"])
        if user==(a+b):
            return render_template("user.html",user='答對')
        else:
            return render_template("user.html",user='答錯')
    else:
        return redirect(url_for("login"))
if __name__ =="__main__":
    app.run()