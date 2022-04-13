import cv2
import sys
from multiprocessing import Process 

from Camera import MotionDetectionCam, ICamera, BlankCamera
from MotionDetection import MDOps

from LocalRun import runBlankCamera, runMotionDetectionCam, runFaceRecognitionCam

from flask import Flask


if __name__ == '__main__':
    # runBlankCamera()
    # runMotionDetectionCam()
    # trainImage()
    runFaceRecognitionCam()
    
