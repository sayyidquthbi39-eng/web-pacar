from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USERNAME = "sayang"
PASSWORD = "123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            return redirect("/home")
        else:
            return "Login gagal!"

    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")