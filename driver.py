import cv2
import sys
from multiprocessing import Process 


from Camera import PorchCam
from MotionDetectionPackage import MDOps

def runPorchCam():
    camera = PorchCam.PorchCam(0)
    detector = MDOps.MDOps()
    while True:
        frame = camera.Capture()
        res = detector.FindLandMark(frame)
        cv2.imshow("Image",res)
        if cv2.waitKey(1) == 32:
            break
    camera.release()    
    cv2.destroyAllWindows()

def runFrontCam():
    pass
    
    
if __name__ == '__main__':
    runPorchCam()
    