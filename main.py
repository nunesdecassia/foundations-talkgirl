from flask import Flask, render_template
from routes.login import render_login

app = Flask(__name__)

# INDEX
@app.route('/')
def index():
    return render_template('index.html', title="GirlTalk")
