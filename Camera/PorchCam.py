import cv2
import sys
import os

from Camera import ICamera
from MotionDetectionPackage import MDOps

class PorchCam(ICamera.ICamera):
    def __init__(self,index):
        self.camera = cv2.VideoCapture(index)
    def Capture(self):
        success, frame = self.camera.read()
        imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.waitKey(1)
        return imgRGB
    def __del__(self):
        self.camera.release()