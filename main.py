from flask import Flask, render_template, request

from routes.dashboard import render_dashboard
from routes.home import render_home
from routes.login import render_login
from routes.signup import handle_signup

app = Flask(__name__)

# HOME
app.add_url_rule('/', 'home', render_home)

# LOGIN
app.add_url_rule('/login', 'login', render_login)

# SIGNUP
app.add_url_rule('/signup', 'signup', handle_signup, methods=['GET', 'POST'])

# DASHBOARD
app.add_url_rule('/dashboard', 'dashboard', render_dashboard)
