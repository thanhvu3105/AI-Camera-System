import cv2
import numpy as np
import time
import os
import os.path

# import the file where data is
# stored in a csv file format
import npwriter
  


#This function detecting faces and saves it to dir "train" with each faces
#comes along with labor
def face_detection():
    #label for supervised training, generate a directory with each person's label and contains his/her images.
    name = str(input("Enter your name: "))
    parent_dir = os.getcwd()
    directory = name
    path_label = os.path.join(parent_dir,"train_dir",directory)
    if(os.path.isdir(path_label) == False):
        os.mkdir(path_label)
    
    
    #camera index
    cap = cv2.VideoCapture(2)
    
    #classifer for face detection
    face_cascade = cv2.CascadeClassifier("../cascades/haarcascade_frontalface_default.xml")
    eyes_cascade = cv2.CascadeClassifier('../cascades/haarcascade_eye.xml')

    #stroing faces 
    faces_list = []
    label_id = 0 

    
    while True:
        #capture frame-by-frame
        ret, frame = cap.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # detect multiscale, detects the face and its coordinates
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5,minNeighbors=3)
        eyes = eyes_cascade.detectMultiScale(frame, scaleFactor=1.5,minNeighbors=3)
        
        faces = sorted(faces,key = lambda x: x[2]*x[3],reverse = True)
        eyes = sorted(eyes,key = lambda x: x[2]*x[3],reverse = True)

        # len(faces) is the number of
        # faces showing in a frame



        if len(faces) == 1:   
            # if len(eyes) > 0:
            for(x,y,w,h) in faces: 
            # face = faces[0]   
            # storing the coordinates of the
            # face in different variables
            # x, y, w, h = face 
            # this is will show the face
            # that is being detected     
                # ROI_face = frame[y:y + h, x:x + w] 
                #drawing rectange on camera.
                color = (255,0,0)  #BGR 0-255
                stroke = 2 #thick
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y), color, stroke)


                key = cv2.waitKey(1)
                if key & 0xFF == ord('c'):
                    #convert to gray face ROI
                    # gray_face = cv2.cvtColor(faces[:1], cv2.COLOR_BGR2GRAY)
                    # gray_face = cv2.resize(gray_face,(500,500))
                    #screenshot and save it training input directory

                    label_id += 1
                    faces_list.append(frame.reshape(-1))
                    print(len(faces_list),type(frame),frame.shape)
                    print("Save to ", path_label)
                    cv2.imwrite(f'{path_label}/{str(label_id)}.jpg',frame)

                    if(label_id == 20):
                        break

                        
                # cv2.imshow("face", im_face)

        if not ret:
            print("faces not detected")
            continue

        cv2.imshow("img", frame)

        if(len(faces_list) == 15):
            time.sleep(2)
            print("Images loads sucessfully")
            break
        if cv2.waitKey(5) == 32:
            break

    cap.release()
    cv2.destroyAllWindows()
    
       
    # declared in npwriter
    # npwriter.write(name, np.array(f_list)) 
    
    
face_detection()