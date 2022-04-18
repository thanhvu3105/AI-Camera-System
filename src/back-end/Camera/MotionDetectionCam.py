import cv2
import sys
import os

from Camera import ICamera
from MotionDetection import MDOps

#motion detection camera
class MotionDetectionCam(ICamera.ICamera):
    def __init__(self,index,cameraName):
        super().__init__(index,cameraName)
    def Capture(self):
        return super().Capture()
    def __del__(self):
        super().__del__()
