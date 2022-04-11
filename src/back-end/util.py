import cv2
import sys
import os.path

from Camera import BlankCamera, FaceRecognitionCam, MotionDetectionCam
from MotionDetection import MDOps
from FaceRecog import FaceRecogOps,face_train
from datetime import datetime


class Query():
    def __init__(self,img,cameraId,date):
        self.img = img
        self.cameraId = cameraId
        self.date = date
    


    

    