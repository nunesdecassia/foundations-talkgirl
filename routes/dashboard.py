from flask import render_template, redirect, session


def render_dashboard():
    user = session.get('user')

    if user is None:
        return redirect('/')

    print('--- RENDERING DASHBOARD ---')
    return render_template('dashboard.html', title='Talkgirl - DASHBOARD', user=user)
