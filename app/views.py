from app import app, mail
from flask_mail import Mail, Message
from flask import Flask, render_template, request

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('about.html')

@app.route('/projects', methods = ['GET'])
def projects():
    return render_template('projects.html')

@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

@app.route('/sent', methods = ['POST', 'GET'])
def send():
    result = request.form
    sent = str(result['sender'])
    email = str(result['mail'])

    msg = Message('Mail from your Website', sender='ronaldocedras@gmail.com', recipients=['rcedras0010@gmail.com'] )
    msg.body = email + '\nFrom ' + sent
    mail.send(msg)

    return '<h1>Message sent</h1>'
