import sys
import cv2
from MotionDetectionPackage import MotionDetectionPackage

class MDOps(MotionDetectionPackage.MotionDetectionPackage):
    def __init__(self,camera):
        super().__init__(camera)

    def FindLandMark(self,cam):
        results = self.holistic.process(cam)
        if(results.pose_landmarks or results.face_landmarks):
            for id,lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = cam.shape
                #PIXEL VALUE
                cx,cy = int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                cv2.circle(cam, (cx,cy), 10,(255,0,255),cv2.FILLED)


            self.mpDraw.draw_landmarks(
                cam,
                results.pose_landmarks,
                self.mpHolistic.POSE_CONNECTIONS,
                landmark_drawing_spec = self.mp_drawing_styles.get_default_pose_landmarks_style()
            )
        return cam
        
    def runMotionDetection(self):
        # while True:
        img = self.FindLandMark(self.camera)
        cv2.imshow("Image",img)

 
            