import ICamera
import cv2

class FrontDoorCam(ICamera.ICamera):
    def __init__(self,index):
        self.camera = cv2.VideoCapture(index)
    def CaptureVideo(self):
        success, frame = self.camera.read()
        imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.waitKey(1)
        return imgRGB
    