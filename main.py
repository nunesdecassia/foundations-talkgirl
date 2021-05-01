from flask import Flask
from uuid import uuid4

from routes.dashboard import render_dashboard
from routes.home import render_home
from routes.login import handle_login
from routes.signup import handle_signup

app = Flask(__name__)
app.secret_key = uuid4().bytes

# HOME
app.add_url_rule('/', 'home', render_home)

# LOGIN
app.add_url_rule('/login', 'login', handle_login, methods=['GET', 'POST'])

# SIGNUP
app.add_url_rule('/signup', 'signup', handle_signup, methods=['GET', 'POST'])

# DASHBOARD
app.add_url_rule('/dashboard', 'dashboard', render_dashboard)


# CUSTOM JINJA FILTERS
@app.template_filter('hashtag')
def create_hashtag(value):
    return '#' + value.replace('-', '').upper()

