import os
from sys import path_importer_cache
from zipfile import Path
import cv2
from PIL import Image

import numpy as np
import pandas as pd
  
from datetime import datetime
from npwriter import f_name
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"testing")


data = pd.read_csv(f_name).values   
    
    # data partition
X, Y = data[:, 1:-1], data[:, -1]
    
print(len(X),len(Y),X,Y)
    
    # # Knn function calling with k = 5
model = KNeighborsClassifier(n_neighbors = 9)
    
    # # fdtraining of model
model.fit(X, Y)

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root,file)
            # label = os.path.basename(root).replace(" ", "-").lower()
            img = cv2.imread(path)
            gray_face = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            X_test = []

            faces = face_cascade.detectMultiScale(gray_face, scaleFactor=1.7,minNeighbors=3)
            for (x,y,w,h) in faces:
                roi_face = gray_face[y:y + h, x:x + w]
                roi_face = cv2.resize(roi_face, (224, 224))
                X_test.append(roi_face.reshape(-1))
    
            if len(faces) == 1:
                # print(path)
                response = model.predict(np.array(X_test))
                for i, (x,y,w,h) in enumerate(faces):
                    print(path,response[i])
                # drawing a rectangle on the detected face
                    # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                # adding detected/predicted name for the face
                    # cv2.putText(frame, response[i], (x-50, y-50), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 3)