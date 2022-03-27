from abc import abstractmethod
import cv2

#abstract camera class
class ICamera():
    @abstractmethod
    def __init__(self,index):
        pass

    @abstractmethod
    def Capture(self):
        pass

    @abstractmethod
    def __del__(self):
        pass