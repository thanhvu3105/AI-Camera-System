import cv2
import time
import mediapipe as mp

class Camera():
    def __init__(self,index):
        self.camera = cv2.VideoCapture(index)
    def Capture(self):
        success,frame = self.camera.read()
        frame.flags.writeable = False
        return frame

class PoseDetection():
    def __init__(self,
        mode=False,
        model=1,
        smooth_landmarks=True,
        enable_seg = False, 
        smooth_seg = False,
        refine_face = False,
        detection_confidence = 0.5,
        tracking_confidence = 0.5
        ):
        
        #declar configurations
        self.mode = mode
        self.model= model
        self.smooth_landmarks= smooth_landmarks
        self.enable_seg = enable_seg
        self.smooth_seg = smooth_seg
        self.refine_face = refine_face
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        # self.camera = camera
        
        #declare API package
        self.mpDraw = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mpHolistic = mp.solutions.holistic
        self.holistic = self.mpHolistic.Holistic(self.mode,self.model,self.smooth_landmarks,self.enable_seg,
                                                self.smooth_seg,self.refine_face,self.detection_confidence,
                                                self.tracking_confidence)
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
                cv2.circle(img, (cx,cy), 10,(255,0,255),cv2.FILLED)


            self.mpDraw.draw_landmarks(
                img,
                result.pose_landmarks,
                self.mpHolistic.POSE_CONNECTIONS,
                # landmark_drawing_spec=None,
                landmark_drawing_spec= self.mp_drawing_styles.get_default_pose_landmarks_style()
            )

        return img



if __name__ == '__main__':
    camera = Camera(0)
    detector = PoseDetection()
    while True:
        frame = camera.Capture()
        res = detector.FindLandMark(frame)
        cv2.imshow("Image", res)
        if cv2.waitKey(1) == 32:
            break
    frame.release()
    cv2.destroyAllWindows()



