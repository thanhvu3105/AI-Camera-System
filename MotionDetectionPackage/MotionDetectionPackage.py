#Motion detection will get whatever motion detection operation is 

import mediapipe as mp

##NOTE: create a child class called MotionDetectionOps class that inhertiance MotionDetect.

class MotionDetectionPackage():
    ##CONSTRUCTOR##
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

        
        #declare API package
        self.mpDraw = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mpHolistic = mp.solutions.holistic
        self.holistic = self.mpHolistic.Holistic(self.mode,self.model,self.smooth_landmarks,self.enable_seg,
                                                self.smooth_seg,self.refine_face,self.detection_confidence,
                                                self.tracking_confidence)
       

    


    