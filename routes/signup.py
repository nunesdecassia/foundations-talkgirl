from flask import render_template, request, redirect
from routes.database import save_user


def handle_signup():
    if request.method == 'POST':
        save_user(request.form)
        return redirect('/')

    print('--- RENDERING SIGNUP ---')
    return render_template('signup.html', title='Talkgirl - SIGNUP')
