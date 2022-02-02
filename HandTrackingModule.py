from xmlrpc.client import SYSTEM_ERROR
import cv2
import time
import mediapipe as mp


class Camera():
    def __init__(self,index):
        self.camera = cv2.VideoCapture(index)
    def CaptureVideo(self):
        success, img = self.camera.read()
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        cv2.waitKey(1)
        return imgRGB
    def closeCamera(self):
        self.camera.release()

class handDetector():
    ### Constructor ###
    def __init__(self,mode=False,maxHands=2,modelComplex = 1,detectionCon=0.75,trackCon=0.75):
        #MP Hands API Configuration
        self.mode=False
        self.maxHands= maxHands
        self.modelComplex= modelComplex
        self.detectionCon= detectionCon
        self.trackCon=trackCon
        
        #Declare API
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelComplex,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        #frame time to calculate FPS
        self.pTime = 0.0
        self.nTime = 0.0

        

    #TODO: parameters is a openCV camera
    #it only draws when we ask it to draw
    def FindLandMark(self,img):
        # img = self.CaptureVideo()
        results = self.hands.process(img)
        if(results.multi_hand_landmarks):
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(
                    img,
                    handLms,
                    self.mpHands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )
        return img
           
    def fps(self):
        self.nTime = time.time()
        fps = 1/(self.nTime - self.pTime)
        pTime = self.nTime
        return fps

       


def main():
    camera = Camera(0)
    detector = handDetector()
    while True:
        img = camera.CaptureVideo()
        detector.FindLandMark(img)
        detector.fps()
        cv2.imshow("Image",img)


if __name__ == "__main__":
    main()