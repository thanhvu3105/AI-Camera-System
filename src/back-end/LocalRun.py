import cv2
import sys
import os.path

from Camera import BlankCamera, FaceRecognitionCam, MotionDetectionCam
from MotionDetection import MDOps
from FaceRecog import FaceRecogOps,face_train
from datetime import datetime
# from insertQuery import insertQuery

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
    camera = MotionDetectionCam.MotionDetectionCam(-1,"Porch Camera")
    detector = MDOps.MDOps()
    
    counter = 0
 
    while True:
        # detected = False
        frame = camera.Capture()
        font = cv2.FONT_HERSHEY_SIMPLEX

        now = datetime.now()
        
        ret, res = detector.FindLandMark(frame)

        #LOGIC FOR SENDING DATA OUT
        if ret == True and counter == 0:
            print("Motion detected")
            counter += 1
            #insert data to query table
            # insertQuery(camera.cameraName,frame,now)
           
        if ret == False:
            print("No motion detected")
            counter = 0
            # imgCapture.clear()

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
        ret,label,frame = detector.recogLBHP(frame)
        
        cv2.imshow("imgage",frame)
        if cv2.waitKey(1) == 32:
            break
    camera.__del__()
        

def sendData(image,date,cameraId):
    pass
