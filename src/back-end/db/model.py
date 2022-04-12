from db import db
from datetime import datetime

class Img(db.Model):
    CameraId = db.Column(db.String)
    Image = db.Column(db.Text, unique=True)
    TimeStamp = db.Column(db.DateTime, nullable=False)

    