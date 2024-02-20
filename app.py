from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

tabs = ["About", "Projects", "Connect"]

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', tabs=tabs)