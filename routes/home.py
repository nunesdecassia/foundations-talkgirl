from flask import render_template

def render_home():
    print('--- RENDERING HOME ---')
    return render_template('home.html', title='Talkgirl - HOME')
    