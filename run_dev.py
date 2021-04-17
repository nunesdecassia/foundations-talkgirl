from main import app

app.config['FLASK_ENV'] = 'development'
app.config['DEBUG'] = True

app.run(port='8080', host='localhost')
