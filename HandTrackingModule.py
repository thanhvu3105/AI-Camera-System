import cv2
import time
import mediapipe as mp

class Camera():
    def __init__(self,camera):
        return

class HandDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.75,trackCon=0.75):
        #Declare API
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        #MP Hands API Configuration
        self.mode=False
        self.maxHands= maxHands
        self.detectionCon= detectionCon
        self.trackCon=trackCon

        #frame time to calculate FPS
        self.pTime = 0.0
        self.nTime = 0.0

    #TODO: parameters is a openCV camera
    #it only draws when we ask it to draw
    def DrawLandMark(self,camera,draw=True):
        cameraRGB = cv2.cvtColor(camera,cv2.COLOR_BGR2RGB)
        results = self.hands.pr


          
    def fps(pTime,nTime):
        nTime = time.time()
        fps = 1/(nTime - pTime)
        pTime = nTime
        return fps




if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0
    main()