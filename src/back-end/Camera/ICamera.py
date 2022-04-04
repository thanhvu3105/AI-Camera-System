from abc import abstractmethod
import cv2

#abstract camera class
class ICamera():
    @abstractmethod
    def __init__(self,index,cameraName):
        self.camera = cv2.VideoCapture(index)
        self.cameraName = cameraName
    @abstractmethod
    def Capture(self):
        success, frame = self.camera.read()
        cv2.waitKey(1)
        return frame
    @abstractmethod
    def __del__(self):
        self.camera.release()
        cv2.destroyAllWindows()