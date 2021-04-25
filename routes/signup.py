from flask import render_template, request, redirect
from routes.database import create_user


def handle_signup():
    if request.method == 'POST':
        create_user(request.form)
        return redirect('/')

    print('--- SIGNUP ---')
    return render_template('signup.html', title='Talkgirl - SIGNUP')
