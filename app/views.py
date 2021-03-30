from app import app, mail
from flask_mail import Mail, Message
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

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
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

