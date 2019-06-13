from bottle import run, route, app


@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


run(app, host='localhost', port=8080)
