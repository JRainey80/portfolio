from flask import Flask, render_template, request, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

nav_items = [
    {'name': 'Home', 'url':'/'},
    {'name': 'About', 'url': '/about'},
    {'name': 'Projects', 'url': '/projects'},
    {'name': 'Connect', 'url': '/connect'}
]

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", nav_items=nav_items)

@app.route("/about", methods=["GET", "POST"] )
def about():
    return render_template("about.html" , nav_items=nav_items)

@app.route("/connect", methods=["GET", "POST"])
def connect():
    return render_template("connect.html", nav_items=nav_items)

@app.route("/projects", methods=["GET", "POST"])
def projects():
    return render_template("projects.html", nav_items=nav_items)

if __name__ == '__main__':
    app.run(debug=True)

