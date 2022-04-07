import sys
import pickle


import cv2
import numpy as np
import pandas as pd
  
from datetime import datetime
from .face_train import train
# from FaceRecog.face_recog_LBHP.face_train import train

class FaceRecogOps:
    def __init__(self):
        self.labels = {"person_name" : 1}
        with open('labels.pkl', 'rb') as f:
            og_labels = pickle.load(f)
            self.labels = {v:k for k,v in og_labels.items()}

        self.model = cv2.face.LBPHFaceRecognizer_create()
        self.model.read("model.yml")

        self.face_cascade = cv2.CascadeClassifier('FaceRecog/cascades/haarcascade_frontalface_alt2.xml')
        self.eyes_cascade = cv2.CascadeClassifier('FaceRecog/cascades/haarcascade_eye.xml')
    def trainImages(self):
        train()

    def recogLBHP(self,camera):
        #read data from csv file
       

        # while(True):
            
        gray = cv2.cvtColor(camera,cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.6,minNeighbors=3)
        eyes = self.eyes_cascade.detectMultiScale(gray, scaleFactor=1.6,minNeighbors=3)

        faces = sorted(faces,key = lambda x: x[2]*x[3],reverse = True)
        eyes = sorted(eyes,key = lambda x: x[2]*x[3],reverse = True)

        if(len(faces) == 1):
            if(len(eyes) > 0):
                for (x,y,w,h) in faces:
                    # print(x,y,w,h)
                    roi_gray = gray[y:y+h,x:x+w]  #[ycord_start, ycord_end]
                    
                    color = (255,0,0)  #BGR 0-255
                    stroke = 2 #thick
                    end_cord_x = x + w
                    end_cord_y = y + h
                    cv2.rectangle(camera,(x,y),(end_cord_x,end_cord_y), color, stroke)


                    face_section = camera[y-10:end_cord_y+10, x-10: end_cord_x+10]              
                    idx, confidence = self.model.predict(roi_gray)
                
                    #LBPH algorithm            
                    accuracy = confidence/(confidence + (100 - confidence))
                                # print(idx, threshold)
                    if(accuracy <= 1):
                        print(idx, self.labels[idx], round(accuracy, 5))
                        cv2.putText(camera,self.labels[idx],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1,cv2.LINE_AA)

                    if(accuracy >= 1.10):
                        cv2.putText(camera,"Intruder",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1,cv2.LINE_AA)


        return camera           