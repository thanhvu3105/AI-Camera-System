import cv2
import sys
import os

from Camera import ICamera
from MotionDetectionPackage import MDOps

class PorchCam(ICamera.ICamera):
    def __init__(self,index):
        #DECREASING THE LAGNESS 
        self.camera = cv2.VideoCapture(index)

    def Cap(self):
        success, frame = self.camera.read()
        imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.waitKey(1)
        return imgRGB
    def run(self):
        #what to do 
        #Get CaptureVideo() -> imgRGB
        # runMotionDetection from Motion Detection Package.
        while True:
            cam = self.Cap() 
            detector = MDOps.MDOps(cam)
            detector.runMotionDetection()
            if(cv2.waitKey(1) == 32):
                break
        self.camera.release()
        cv2.destroyAllWindows()