from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

tabs = ["About", "Projects", "Connect"]

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', tabs=tabs)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/connect")
def connect():
    return render_template("connect.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")