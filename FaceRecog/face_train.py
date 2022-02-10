import os
import cv2
import pickle
from PIL import Image
import numpy as np

# ###NOTE: work flow wuold be like. 
#     - You read a frame, using cap.read()
#     - Optionally, you can convert to different kind of colors
#     - then you perform face casade to do face detection.
#     - extract pixels value from it, with x,y is starting coord, w,h is ending coord
#     - then you need to create a Region Of Interest(ROI), using formula:
#         - ROI = image_file[y:y+h,x:x+h]

#Return the current dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"known_faces")

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root,file)
            label = os.path.basename(root).replace(" ", "-").lower()
            #label: name dir
            #path: pwd         
            # print(label,path)

            ###CREATING ID FOR EACH PERSON
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]

            #open the file within the path
            pil_image = Image.open(path,mode='r').convert("L") #Gray scale image
            # print(pil_image)
            #taking every pixels value turns into numpy array
            image_array = np.array(pil_image, "uint8")
                                   ##We do face detection for those images
            # print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.6,minNeighbors=3)
            # print(faces)
            for(x,y,w,h) in faces:
                # print(image_array)
                roi = image_array[y:y+h,x:x+w]
                print(roi)
                # print(roi)    
                x_train.append(roi)
                y_labels.append(id_)

# print(y_labels)
 
# for i in range(0,x_train.size()):
#     print(y_labels[i], x_train[i])


with open("labels.pkl",'wb') as f:
    pickle.dump(label_ids,f)


