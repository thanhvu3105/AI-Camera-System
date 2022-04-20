from flask import Flask, render_template, request   , Response
from flask_bootstrap import Bootstrap
from FaceRecog import FaceRecogOps, face_train

from Camera import BlankCamera, FaceRecognitionCam, MotionDetectionCam
from ServerOps import genSkeleton, genRecog
from MotionDetection import MDOps

import cv2
import os
import sqlite3

from datetime import datetime

# MODE = os.getenv('FLASK_ENV')


app = Flask(__name__)
bootstrap = Bootstrap(app)

# Enter your database connection details below
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite")
conn = sqlite3.connect(db_path, check_same_thread=False)

cursor_setup = conn.cursor()
cursor_setup.execute('CREATE TABLE IF NOT EXISTS reportedAlerts(camera_id integer, camera_name text, person_id text, timestamp text)')
conn.commit()

#Default pages
@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reportedAlerts WHERE camera_id = 1')
    reports = cursor.fetchall()
    return render_template('index.html', reports=reports)


@app.route('/2')
def index2():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reportedAlerts WHERE camera_id = 2')
    reports = cursor.fetchall()
    return render_template('index2.html', reports=reports)



# For Camera 1
@app.route('/video_feed', methods=['GET'])
def video_feed():
    camera = MotionDetectionCam.MotionDetectionCam(0, "Porch Camera")
    return Response(genSkeleton(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

# For Camera 2
@app.route('/video_feed2', methods=['GET'])
def video_feed2():
    camera = FaceRecognitionCam.FaceRecognitionCam(-1, "Door Camera")
    return Response(genRecog(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

#Run the host server
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)
