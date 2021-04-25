from flask import render_template


def render_dashboard():
    print('--- RENDERING DASHBOARD ---')
    return render_template('dashboard.html', title='Talkgirl - DASHBOARD')
