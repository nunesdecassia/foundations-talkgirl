from flask import render_template, request, redirect


def handle_signup():
    if request.method == 'POST':
        print(request.form)
        return redirect('/')

    print('--- RENDERING SIGNUP ---')
    return render_template('signup.html', title='Talkgirl - SIGNUP')
