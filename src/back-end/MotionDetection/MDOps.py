import sys
import cv2
from MotionDetection import MotionDetectionPackage
from datetime import datetime



class MDOps(MotionDetectionPackage.MotionDetectionPackage):
    def __init__(self):
        super().__init__()
        self.detected = False
        self.capture = []
        
    def FindLandMark(self,camera):
        # img = super().Capture()        
        
        img = cv2.cvtColor(camera,cv2.COLOR_BGR2RGB)
        result = self.holistic.process(img)
        
        detected = False

        if(result.pose_landmarks or result.face_landmarks):
        #Draw Pose
            # print("Motion detected",len(self.capture))
            if len(self.capture) < 2:
                self.capture.append(camera)
                detected = True
 
            self.mpDraw.draw_landmarks(
                img,
                result.pose_landmarks,
                self.mpHolistic.POSE_CONNECTIONS,
                # landmark_drawing_spec=None,
                landmark_drawing_spec= self.mp_drawing_styles.get_default_pose_landmarks_style()
            )

            # dataObj = Data(self.capture[0],cameraID, datetime.now())
            return True,img

        else:
            return False, img

        # return img
        

        
      
        
    
 
            