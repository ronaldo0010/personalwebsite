from app import app, mail
from flask_mail import Mail, Message
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask import send_file


@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('about.html')

@app.route('/projects', methods = ['GET'])
def projects():
    return render_template('projects.html')

@app.route('/sent', methods = ['POST', 'GET'])
def send():
    result = request.form
    sent = str(result['sender'])
    email = str(result['mail'])

    msg = Message('Mail from your Website', sender='ronaldocedras@gmail.com', recipients=['rcedras0010@gmail.com'] )
    msg.body = email + '\nFrom ' + sent
    mail.send(msg)

    return '<h1>Message sent</h1>'


@app.route('/upload')
def submit_file():
   return render_template('upload.html')
	

@app.route('/ass_down', methods = ['GET', 'POST'])
def download():
    path = "../wb272-tut00-data.tar.bz2"
    return send_file(path, as_attachment=True)