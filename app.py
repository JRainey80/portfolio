from flask import Flask, render_template, request, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

tabs = ["About", "Projects", "Connect", "Home"]

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", title="Justin Rainey - Portolio", tabs=tabs)

@app.route("/about", methods=["GET", "POST"] )
def about():
    return render_template("about.html")

@app.route("/connect", methods=["GET", "POST"])
def connect():
    return render_template("connect.html")

@app.route("/projects", methods=["GET", "POST"])
def projects():
    return render_template("projects.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template('index.html')

