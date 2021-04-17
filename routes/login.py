from flask import render_template

def render_login():
    print('--- RENDERING LOGIN ---')
    return render_template('login.html', title='Talkgirl - LOGIN')
    