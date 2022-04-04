import cv2
import time
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


mpPose = mp.solutions.pose
pose = mpPose.Pose()
# holistic = mpHolistic.Holistic() 

cap = cv2.VideoCapture(0)

## We can change resolution of camera
# def make_480p():
#     cap.set(3,640)
#     cap.set(4,480)


while True:

    success,img = cap.read()
    img.flags.writeable = False
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(img)

    if(result.pose_landmarks or result.face_landmarks):
        #Draw Pose
        for id,lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = img.shape
            #PIXEL VALUE
            cx,cy = int(lm.x*w),int(lm.y*h)
            print(id,cx,cy)
            cv2.circle(img, (cx,cy), 10,(255,0,255),cv2.FILLED)


        mpDraw.draw_landmarks(
            img,
            result.pose_landmarks,
            mpPose.POSE_CONNECTIONS,
            # landmark_drawing_spec=None,
            landmark_drawing_spec= mp_drawing_styles.get_default_pose_landmarks_style()
        )



        # #Draw Face
        # mpDraw.draw_landmarks(
        #     img,
        #     result.face_landmarks,
        #     mpHolistic.FACEMESH_CONTOURS,
        #     landmark_drawing_spec=None,
        #     connection_drawing_spec= mp_drawing_styles.get_default_face_mesh_contours_style()
        # )
    

    cv2.imshow("Image",img)
    if cv2.waitKey(1) == 32:
        break

cap.release()
cv2.destroyAllWindows() 


