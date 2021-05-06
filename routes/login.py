from flask import render_template, request, redirect, session
from routes.database import authenticate


def handle_login():
    error = None

    if request.method == 'POST':
        user = authenticate(request.form)

        if user:
            session['user'] = user
            return redirect('/dashboard')
        else:
            error = "This email/password combination is not valid."

    print('--- LOGIN ---')
    return render_template('login.html', title='Talkgirl - LOGIN', error=error)


def handle_logout():
    session.pop('user')
    return redirect('/login')
