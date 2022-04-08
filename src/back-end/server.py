from flask import Flask, render_template, url_for, Response
from flask_bootstrap import Bootstrap
from Operations import runBlankCamera, runMotionDetectionCam
from FaceRecog import FaceRecogOps, face_train

from Camera import BlankCamera, FaceRecognitionCam, MotionDetectionCam
from MotionDetection import MDOps
import cv2
import os

from datetime import datetime

# MODE = os.getenv('FLASK_ENV')
# DEV_SERVER_URL = 'http://localhost:3000/'

# TO DO: FIND CLIENT FOLDER WITHOUT HARD CODING THE PATH.
# templateDir = os.path.abspath("/home/thanh/Desktop/computer_vision/project_workspace/src/front-end/src")
# templateDir = os.path.abspath("/home/thanh/Desktop/computer_vision/project_workspace/src/back-end/client")

app = Flask(__name__)
bootstrap = Bootstrap(app)


# if MODE == "development":
#     app = Flask(__name__, static_folder=None)

def gen(camera):
    while True:
        frame = camera.Capture()
        frameName = "cam.jpg"
        cv2.imwrite(frameName, frame)
        frame = open(frameName, 'rb').read()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def gen2(camera):
    detector = MDOps.MDOps()
    while True:
        frame = camera.Capture()
        frame = detector.FindLandMark(frame)

        font = cv2.FONT_HERSHEY_SIMPLEX
        now = datetime.now()
        cv2.putText(frame, str(now.replace(microsecond=0)), (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        frameName = "Motion.jpg"
        cv2.imwrite(frameName, frame)
        frame = open(frameName, 'rb').read()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

   
def gen3(camera):    

    detector = FaceRecogOps.FaceRecogOps()
    while True:
        frame = camera.Capture()
        frame = detector.recogLBHP(frame)
        # ret,jpeg = cv2.imencode("face.jpg",frame)
        frameName = "Face.jpg"
        cv2.imwrite(frameName, frame)
        frame = open(frameName, 'rb').read()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

       

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
    return Response(gen2(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

# For Camera 2
@app.route('/video_feed2', methods=['GET'])
def video_feed2():
    camera = FaceRecognitionCam.FaceRecognitionCam(cv2.CAP_V4L2, "Door Camera")
    return Response(gen3(camera), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)