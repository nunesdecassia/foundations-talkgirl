from flask import render_template, redirect


def render_home():
    print('--- RENDERING HOME ---')
    return redirect("/dashboard")
    # return render_template('home.html', title='Talkgirl - HOME')
