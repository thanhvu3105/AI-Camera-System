import sys
import cv2
from MotionDetection import MotionDetectionPackage
from datetime import datetime


class MDOps(MotionDetectionPackage.MotionDetectionPackage):
    def __init__(self):
        super().__init__()

    def FindLandMark(self,camera):
        # img = super().Capture()
        img = cv2.cvtColor(camera,cv2.COLOR_BGR2RGB)
        result = self.holistic.process(img)
        
       
        
        if(result.pose_landmarks or result.face_landmarks):
        #Draw Pose
            for id,lm in enumerate(result.pose_landmarks.landmark):
                h, w, c = img.shape
                #PIXEL VALUE
                cx,cy = int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                # cv2.circle(img, (cx,cy), 10,(255,0,255),cv2.FILLED)

            self.mpDraw.draw_landmarks(
                img,
                result.pose_landmarks,
                self.mpHolistic.POSE_CONNECTIONS,
                # landmark_drawing_spec=None,
                landmark_drawing_spec= self.mp_drawing_styles.get_default_pose_landmarks_style()
            )

        return img
        
    
 
            