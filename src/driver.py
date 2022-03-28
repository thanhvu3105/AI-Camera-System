import cv2
import sys
from multiprocessing import Process 

from Camera import MotionDetectionCam, ICamera, BlankCamera
from MotionDetection import MDOps

from Operations import runBlankCamera, runMotionDetectionCam, runFaceRecognitionCam


if __name__ == '__main__':
    # runBlankCamera()
    runMotionDetectionCam()
    