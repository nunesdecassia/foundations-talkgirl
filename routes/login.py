from flask import render_template, request, redirect, session
from routes.database import authenticate


def handle_login():
    if request.method == 'POST':
        user = authenticate(request.form)

        if user:
            session['user'] = user
            return redirect('/dashboard')

    print('--- LOGIN ---')
    return render_template('login.html', title='Talkgirl - LOGIN')
