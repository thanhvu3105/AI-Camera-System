
import cv2
from dotenv import load_dotenv
import numpy as np

from LocalRun import runBlankCamera, runMotionDetectionCam
from FaceRecog import FaceRecogOps, face_train


from MotionDetection import MDOps

from datetime import datetime

import os   
import sqlite3
    

from twilio.rest import Client

load_dotenv()
accountSID = os.getenv('SID')
authToken = os.getenv('TOKEN')
client = Client(accountSID, authToken)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite")
conn = sqlite3.connect(db_path, check_same_thread=False)

def sendMMS(message):
     client.api.account.messages.create(
                to="+17143093638",
                from_="+19375073705",
                body=message,
            )



def gen(camera):
    while True:
        frame = camera.Capture()
        frameName = "cam.jpg"
        cv2.imwrite(frameName, frame)
        frame = open(frameName, 'rb').read()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def genSkeleton(camera):
    
    detector = MDOps.MDOps()
    counter = 0
    while True:
        frame = camera.Capture()
        ret, frame = detector.FindLandMark(frame)

        font = cv2.FONT_HERSHEY_SIMPLEX
        now = datetime.now()
        cv2.putText(frame, str(now.replace(microsecond=0)), (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cameraID = 1
        camera_name = camera.cameraName
        time_cap = str(now.replace(microsecond=0))

    

        frameName = "Motion.jpg"
        # print(capturedTime)
        cv2.imwrite(frameName, frame)

        if ret == True and counter == 0:
            counter += 1
            # cursor = conn.cursor()
            conn.execute('INSERT INTO reportedAlerts(camera_id, camera_name, person_id, timestamp) VALUES (?, ?, null, ?)', (cameraID, camera_name, time_cap,))
            conn.commit()

            message = f"{camera_name} detects a person, please check your application's report"
            sendMMS(message)

        if ret == False:
            counter = 0
            print("No motion detected")

        frame = open(frameName, 'rb').read()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    


    
   
def genRecog(camera):    
    detector = FaceRecogOps.FaceRecogOps()
    counter = 0
    while True:
        frame = camera.Capture()
        ret,label,frame = detector.recogLBHP(frame)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        now = datetime.now()
        cv2.putText(frame, str(now.replace(microsecond=0)), (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cameraID = 2
        camera_name = camera.cameraName
        time_cap = str(now.replace(microsecond=0))


        if ret == True and counter == 0:
            counter += 1
            conn.execute('INSERT INTO reportedAlerts(camera_id, camera_name, person_id, timestamp) VALUES (?, ?, ?, ?)', (cameraID, camera_name,label ,time_cap,))
            conn.commit()

            message = f"{camera_name} detects {label} at the door, please check your application's report"
            sendMMS(message)

        if ret == False:
            counter = 0
            print("No motion detected")

        frameName = "Face.jpg"
        cv2.imwrite(frameName, frame)
        frame = open(frameName, 'rb').read()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        