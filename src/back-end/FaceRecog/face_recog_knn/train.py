import numpy as np
import npwriter
import os
import cv2
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"train_dir")
ITER = 15

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')


def train():
    label_ids = {}
    current_id = 0
    labels_path = []
    x_train = []
    counter = 0
    label = ""

    for root,dirs,files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
                path = os.path.join(root,file)
                label = os.path.basename(root).replace(" ", "-").lower()




                frame = cv2.imread(path)
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5,minNeighbors=3)
                if(len(faces) == 1):
                    print(path)
                    # print("faces detected")
                    for(x,y,w,h) in faces:
                        # img_face = frame[y:y+h,x:x+w]
                        # gray_faces = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        gray_faces = cv2.resize(frame,(224,224), fx=0.5,fy=0.5,interpolation = cv2.INTER_AREA)
                        counter += 1
                        print(label,counter,len(x_train),type(gray_faces),gray_faces.shape)

                        x_train.append(gray_faces.reshape(-1))
                        # label_ids[label] = x_train
                else:
                    pass
                    # print("no faces found")

        if x_train:
            npwriter.write(label,np.array(x_train))
            # print(label,x_train)
            # x_train.clear()

train()
