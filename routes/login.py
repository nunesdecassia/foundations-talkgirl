from flask import render_template, request, redirect
from routes.database import authenticate


def handle_login():
    if request.method == 'POST':
        if authenticate(request.form):
            return redirect('/dashboard')

    print('--- LOGIN ---')
    return render_template('login.html', title='Talkgirl - LOGIN')
