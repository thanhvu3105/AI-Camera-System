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
#     -  ROI = image_file[y:y+h,x:x+h]

#Return the current dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"known_faces")

def train():

    face_cascade = cv2.CascadeClassifier('FaceRecog/cascades/haarcascade_frontalface_default.xml')

    model = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []
    

    for root,dirs,files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
                path = os.path.join(root,file)
                label = os.path.basename(root).replace(" ", "-").lower()

               
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]

                img = Image.open(path).convert('L')
                final_img = img.resize((224,224),Image.ANTIALIAS)
                img_np = np.array(final_img,'uint8')
                # print(img_np)
                # print(img.shape)
                faces = face_cascade.detectMultiScale(img_np, scaleFactor=1.6,minNeighbors=3)
                
                if len(faces) > 0:
                    for(x,y,w,h) in faces:
                        print(label,path)
                        # print(image_array)
                        img_train = img_np[y:y+h,x:x+w] 
                        # img_np = cv2.resize(img,(224,224))
                        x_train.append(img_train)
                        y_labels.append(id_)
                
    print(y_labels,x_train)

    with open("labels.pkl",'wb') as f:
        pickle.dump(label_ids,f)

    model.train(x_train,np.array(y_labels))
    model.save("model.yml")

