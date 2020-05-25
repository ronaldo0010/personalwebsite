from flask import Flask
from flask_mail import Mail, Message
import smtplib


app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'rcedras0010@gmail.com',
    MAIL_PASSWORD = 'insert_enviorment_variable'
)

mail = Mail(app)

from app import views
