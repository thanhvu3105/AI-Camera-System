# this one is used to recognize the 
# face after training the model with
# our data stored using knn
from inspect import FrameInfo
import cv2
import numpy as np
import pandas as pd
  
from datetime import datetime
from npwriter import f_name
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def knn_recog(cameraIndex):
    # reading the data
    data = pd.read_csv(f_name).values   
    
    # data partition
    X, Y = data[:, 1:-1], data[:, -1]
    
    print(len(X),len(Y),X,Y)
    
    # # Knn function calling with k = 5
    model = KNeighborsClassifier(n_neighbors = 5)
    
    # # fdtraining of model
    model.fit(X, Y)
    
    cap = cv2.VideoCapture(cameraIndex)
    
    face_cascades = cv2.CascadeClassifier("../cascades/haarcascade_frontalface_alt.xml")
    
    f_list = []
    
    while True:
        ret, frame = cap.read()
        gray_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascades.detectMultiScale(gray_face, 1.5, 3)
        X_test = []
        font = cv2.FONT_HERSHEY_SIMPLEX
        now = datetime.now()
        cv2.putText(frame,str(now.replace(microsecond=0)),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
    
        # Testing data
        for (x,y,w,h) in faces:
            roi_face = gray_face[y:y + h, x:x + w]
            roi_face = cv2.resize(roi_face, (100, 100))
            X_test.append(roi_face.reshape(-1))
    
        if len(faces) == 1:
            response = model.predict(np.array(X_test))
            for i, (x,y,w,h) in enumerate(faces):
                # drawing a rectangle on the detected face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                # adding detected/predicted name for the face
                cv2.putText(frame, response[i], (x-50, y-50), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 3)
        
        cv2.imshow("full", frame)
    
        key = cv2.waitKey(1)
    
        if key & 0xFF == ord("q") :
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
knn_recog(0)
    
