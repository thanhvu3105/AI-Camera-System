import numpy as np
import cv2

#Haarcasade_frontalface_alt is an XML file
#containing serialized Haar cascade detector of faces (Viola-Jones algorithm) in the OpenCV library.
#It is coded list of decision trees in which each vertex test one Haar Feature 
#and each list claims “this is not face” or “this could be face”. 
# It can be used the check that a part of image is face. 


face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
eyes_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)


while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.20,minNeighbors=2)
    eyes = eyes_cascade.detectMultiScale(gray, scaleFactor=1.20,minNeighbors=4)

    #detects eyes
    for (ex,ey,ew,eh) in eyes:
        roi_gray = gray[ey:ey+eh,ex:ex+ew]
        end_cord_ex = ex + ew
        end_cord_ey = ey + eh
        cv2.rectangle(frame,(ex,ey),(end_cord_ex,end_cord_ey),(0,128,0),1)

    for (x,y,w,h) in faces:
        # print(x,y,w,h)
        #region of interest
        #This will capture the ROI, which narrow more focus on the face region
        #calculate actual pixel value of item
        roi_gray = gray[y:y+h,x:x+w]  #[ycord_start, ycord_end]
        # roi_color = frame[y:y+h,x:x+w]

        print(roi_gray)

        #RECOGNIZE REGION OF INTERESTS
        #Deep learned model predict keras tensorflow
        
        #screen capture gray color
        cv2.imwrite("gray-screenshot.png",roi_gray)
        #screen capture reg color
        #press c to screenshot
        # cv2.imwrite("screenshot.png", roi_color)  


        color = (255,0,0)  #BGR 0-255
        stroke = 2 #thick
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y), color, stroke)


    #Display resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(5) == 32:
        break


cap.release()
cv2.destroyAllWindows() 



