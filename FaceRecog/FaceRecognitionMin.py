import numpy as np
import cv2
import pickle
from PIL import Image
from numpy import asarray
# import npwriter

#Haarcasade_frontalface_alt is an XML file
#containing serialized Haar cascade detector of faces (Viola-Jones algorithm) in the OpenCV library.
#It is coded list of decision trees in which each vertex test one Haar Feature 
#and each list claims “this is not face” or “this could be face”. 
# It can be used the check that a part of image is face. 

isDetected = False
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
# face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
model = cv2.face.LBPHFaceRecognizer_create()
skip = 0
model.read("model.yml")
labels = {"person_name" : 1}
with open("labels.pkl", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.6,minNeighbors=2)
    eyes = eyes_cascade.detectMultiScale(gray, scaleFactor=1.6,minNeighbors=2)

    # this is used to detect the face which
    # is closest to the web-cam on the first position
    faces = sorted(faces,key = lambda x: x[2]*x[3],reverse = True)
    eyes = sorted(eyes,key = lambda x: x[2]*x[3],reverse = True)
    
    
    if(len(faces) > 0):
        if(len(eyes) > 0):
            
           
            for (x,y,w,h) in faces:
                # print(x,y,w,h)
                roi_gray = gray[y:y+h,x:x+w]  #[ycord_start, ycord_end]
                roi_color = frame[y:y+h,x:x+w] 
                cv2.imwrite("screenshot.png",roi_color)
                
                color = (255,0,0)  #BGR 0-255
                stroke = 2 #thick
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y), color, stroke)


                # face_section = frame[y-10:end_cord_y+10, x-10: end_cord_x+10]              
                # idx, confidence = model.predict(roi_gray)
                

                #import image to numpy array to compare with the training set.
                # skip += 1
                # if(skip % 10 == 0):
                #     face_data = asarray(face_section)
                #     face_data.tofile("face_section.csv",sep=',',format='%10.5f')
                #     if(len(face_data == 10)):
                #         isDetected = True
                #         break

                #LBPH algorithm            
                # accuracy = confidence/(confidence + (100 - confidence))
                #             # print(idx, threshold)
                # # if(accuracy <= 0.):
                # print(idx, labels[idx] , round(accuracy, 5))
                # cv2.putText(frame,labels[idx],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1,cv2.LINE_AA)
    
    if(isDetected == True):
        pass

    #Display resulting frame

    cv2.imshow('frame',frame)
    if cv2.waitKey(5) == 32:
        break



# face_data = np.array(face_data)
# face_data = face_data.reshape((face_data[0],-1))
# np.save('./data' + )

cap.release()
cv2.destroyAllWindows() 



