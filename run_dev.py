from main import app

app.jinja_env.auto_reload = True
app.config.update(
    FLASK_ENV='development',
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)

app.run(port='8080', host='localhost')
