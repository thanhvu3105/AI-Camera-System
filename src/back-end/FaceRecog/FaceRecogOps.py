import sys

from face_recog_knn.knn_recog import knn_recog
from face_recog_knn.train import train 
from face_recog_knn.npwriter import f_name



from inspect import FrameInfo
import cv2
import numpy as np
import pandas as pd
  
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class FaceRecogOps:
    def __init__(self):
        pass
    def trainImages(self):
        train()
    def face_recog(self,camera):
        #read data from csv file
        data = pd.read_csv(f_name).values

        #data partition by
        X, Y = data[:,1:-1], data[:, -1]

        print(len(X),len(Y),X,Y)

        model = KNeighborsClassifier(n_neighbors = 5)

        model.fit(X,Y)


        face_cascades = cv2.CascadeClassifier("cascades/haarcascade_frontalface_alt.xml")
        
