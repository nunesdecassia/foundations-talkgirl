from flask import render_template, request, redirect, session
from routes.database import create_user


def handle_signup():
    if request.method == 'POST':
        user = create_user(request.form)
        session['user'] = user
        return redirect('/dashboard')

    print('--- SIGNUP ---')
    return render_template('signup.html', title='Talkgirl - SIGNUP')
