import cv2

from LocalRun import runBlankCamera, runMotionDetectionCam
from FaceRecog import FaceRecogOps, face_train

from Camera import BlankCamera, FaceRecognitionCam, MotionDetectionCam
from MotionDetection import MDOps

from datetime import datetime


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
        frame = detector.FindLandMark(frame)

        font = cv2.FONT_HERSHEY_SIMPLEX
        now = datetime.now()
        cv2.putText(frame, str(now.replace(microsecond=0)), (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        frameName = "Motion.jpg"
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
        