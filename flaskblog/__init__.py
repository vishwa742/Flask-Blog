from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import cv2
from imutils.video import WebcamVideoStream

app =  Flask(__name__,template_folder='template')
app.config['SECRET_KEY'] = #Enter a secret key here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category = 'info'

class VideoCamera(object):
    def __init__(self):
        self.stream = WebcamVideoStream(src=1).start()

    def __del__(self):
        self.stream.stop()

    def get_frame(self):
        image = self.stream.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        data = []
        data.append(jpeg.tobytes())
        return data

from flaskblog import routes
