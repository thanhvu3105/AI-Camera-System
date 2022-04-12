import cv2
import numpy as np
import base64

from LocalRun import runBlankCamera, runMotionDetectionCam
from FaceRecog import FaceRecogOps, face_train

from Camera import BlankCamera, FaceRecognitionCam, MotionDetectionCam
from MotionDetection import MDOps

from datetime import datetime
from server import testdb

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

        if ret == True and counter == 0:
            counter += 1
            _,framedb = cv2.imencode(".jpg",frame)
            framedb = base64.b64encode(framedb)
            bufDecode = base64.b64decode(framedb)
            nparr = np.fromstring(bufDecode, np.uint8)
            img_np = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
    
            #this is where to send data to D

            print(type(img_np))
            print("Motion detected")
        if ret == False:
            counter = 0
            print("No motion detected")


        frameName = "Motion.jpg"
        # print(capturedTime)
        cv2.imwrite(frameName, frame)
        frame = open(frameName, 'rb').read()


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
        