from Camera import ICamera
import cv2

#Blank Camera 
class BlankCamera(ICamera.ICamera):
    def __init__(self,index,cameraName):
        super().__init__(index,cameraName)
    def Capture(self):
        return super().Capture()
    def __del__(self):
        super().__del__()
    
