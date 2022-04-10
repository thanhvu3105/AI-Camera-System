import cv2
import sys
import os.path

from Camera import BlankCamera, FaceRecognitionCam, MotionDetectionCam
from MotionDetection import MDOps
from FaceRecog import FaceRecogOps,face_train

def runBlankCamera():
    camera = BlankCamera.BlankCamera(0,"Blank Camera")
    while True:
        frame = camera.Capture()
        cv2.imshow("Blank Camera", frame)
        if cv2.waitKey(1) == 32:
            break
    camera.__del__()



#PORCH CAM PICKS MOTION DECTECTION.
#IF USER PICK CAM WITH MOTION DETECTION
def runMotionDetectionCam():
    # camera = ICamera.ICamera(0)   
    camera = MotionDetectionCam.MotionDetectionCam(0,"Porch Camera")
    detector = MDOps.MDOps()
    while True:
        frame = camera.Capture()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        res = detector.FindLandMark(frame)
        cv2.imshow("Image",res)
        if cv2.waitKey(1) == 32:
            break
    camera.__del__()


# def trainImage():
    # FaceRecogOps.trainImages()

#DOOR CAMP TO DO FACE DETECTION
def runFaceRecognitionCam():
    camera = FaceRecognitionCam.FaceRecognitionCam(0,"Door Camera")
    # if not os.path.isfile("FaceRecog/labels.pkl"):
        # face_train.train()
    detector = FaceRecogOps.FaceRecogOps()
    while True:
        frame = camera.Capture()
        res = detector.recogLBHP(frame)
        cv2.imshow("imgage",res)
        if cv2.waitKey(1) == 32:
            break
    camera.__del__()
        