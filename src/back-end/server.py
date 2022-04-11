from flask import Flask, render_template, url_for, Response
from flask_bootstrap import Bootstrap
from Operations import runBlankCamera, runMotionDetectionCam
from FaceRecog import FaceRecogOps, face_train

from Camera import BlankCamera, FaceRecognitionCam, MotionDetectionCam
from ServerOps import genSkeleton, genRecog
from MotionDetection import MDOps
import cv2
import os

from datetime import datetime

# MODE = os.getenv('FLASK_ENV')


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/2')
def index2():
    return render_template('index2.html')


@app.route('/statistics')
def statistics():
    return render_template('stats.html')
    

# For Camera 1
@app.route('/video_feed', methods=['GET'])
def video_feed():
    camera = MotionDetectionCam.MotionDetectionCam(0, "Porch Camera")
    return Response(genSkeleton(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

# For Camera 2
@app.route('/video_feed2', methods=['GET'])
def video_feed2():
    camera = FaceRecognitionCam.FaceRecognitionCam(0, "Door Camera")
    return Response(genRecog(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

# For Camera 3
@app.route('/video_feed3', methods=['GET'])
def video_feed3():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)