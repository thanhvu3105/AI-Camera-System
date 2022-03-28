from Camera import ICamera
import cv2

class FaceRecognitionCam(ICamera.ICamera):
    def __init__(self,index,cameraName):
        super().__init__(index,cameraName)
    def CaptureVideo(self):
        return super().Capture()
    def __del__(self):
        super().__del__()
    