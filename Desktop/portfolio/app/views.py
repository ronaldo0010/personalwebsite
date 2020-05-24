from app import app 

@app.route('/')
def index():
    return 'hello world!'

@app.route('/about')
def about():
    return '<h1>Hello about</h1>'
