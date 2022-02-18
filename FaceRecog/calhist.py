import cv2
import numpy as numpy


img = cv2.imread("Brad_Pitt_Fury_2014.jpg")
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.20,minNeighbors=2)


# color = cv2.cvtColor(img,cv2.IMREAD_ANYCOLOR)
cv2.imshow("image",faces)
cv2.waitKey(0)