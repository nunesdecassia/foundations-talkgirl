from flask import render_template

def render_signup():
    print('--- RENDERING SIGNUP ---')
    return render_template('signup.html', title='Talkgirl - SIGNUP')
    