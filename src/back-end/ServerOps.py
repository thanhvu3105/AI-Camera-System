import cv2

from LocalRun import runBlankCamera, runMotionDetectionCam
from FaceRecog import FaceRecogOps, face_train

from Camera import BlankCamera, FaceRecognitionCam, MotionDetectionCam
from MotionDetection import MDOps

from datetime import datetime

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite")
conn = sqlite3.connect(db_path, check_same_thread=False)

def gen(camera):
    while True:
        frame = camera.Capture()
        frameName = "cam.jpg"
        cv2.imwrite(frameName, frame)
        frame = open(frameName, 'rb').read()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def genSkeleton(camera):
    detector = MDOps.MDOps()
    while True:
        frame = camera.Capture()
        ret, frame = detector.FindLandMark(frame)
        cameraID = 1

        font = cv2.FONT_HERSHEY_SIMPLEX
        now = datetime.now()
        cv2.putText(frame, str(now.replace(microsecond=0)), (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        time_cap = str(now.replace(microsecond=0))

        frameName = "Motion.jpg"
        cv2.imwrite(frameName, frame)
        frame = open(frameName, 'rb').read()

        cursor = conn.cursor()
        conn.execute('INSERT INTO reportedAlerts(camera_id, image, timestamp) VALUES (?, ?, ?)', (cameraID, sqlite3.Binary(frame), time_cap,))
        conn.commit()

        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
   
def genRecog(camera):    
    detector = FaceRecogOps.FaceRecogOps()
    while True:
        frame = camera.Capture()
        frame = detector.recogLBHP(frame)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        now = datetime.now()
        cv2.putText(frame, str(now.replace(microsecond=0)), (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        frameName = "Face.jpg"
        cv2.imwrite(frameName, frame)
        frame = open(frameName, 'rb').read()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        