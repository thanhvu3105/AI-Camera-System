import numpy as np
import npwriter
import os
import cv2
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"train_dir")
ITER = 9

face_cascade = cv2.CascadeClassifier('../cascades/haarcascade_frontalface_alt.xml')


def get_data():
    label_ids = {}
    current_id = 0
    labels_path = []
    x_train = []
    counter = 0

    for root,dirs,files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
                path = os.path.join(root,file)
                label = os.path.basename(root).replace(" ", "-").lower()

                frame = cv2.imread(path)
                faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5,minNeighbors=3)
                if(len(faces) == 1):
                    # print("faces detected")
                    for(x,y,w,h) in faces:
                        img_face = frame[y:y+h,x:x+w]
                        gray_faces = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        gray_faces = cv2.resize(gray_faces,(100,100))
                        counter += 1
                        print(label,counter,len(x_train),type(gray_faces),gray_faces.shape)

                        x_train.append(gray_faces.reshape(-1))
                else:
                    print("no faces found")

                if counter == ITER:
                    label_ids[label] = x_train
                    counter = 0
                    x_train = []
                    break
                

    for key,value in label_ids.items():
        # print(key,value)    
        npwriter.write(key,np.array(value))
                   
                           
  


get_data()