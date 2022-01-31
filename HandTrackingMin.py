import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

pTime = 0
cTime = 0

while True: 
    #Mp.hands solution API configuration
    static_image_mode=True
    max_num_hands = 2
    min_detection_confidence = 0.75    

    #processing camera
    sucess, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    #calculating FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(220,0,205),5)
    
    #check if there is one or multiple hands, if true, extract hand(handLms) one by one
    if (results.multi_hand_landmarks):
        for handLms in results.multi_hand_landmarks:
            #this will draw the hand connection
            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
                )
            #print out correspoding 
        for id,lm in enumerate(handLms.landmark):
            #each ID corresponding to landmark(x,y,z)
            # print(id,lm)
            #row,col,channels
            h,w,c = img.shape 
            #position of center of landmark(x,y,z)
            cx, cy = int(lm.x*w),int(lm.y*h)
            print(id,cx,cy)
            if id == 4:
                cv2.circle(img, (cx,cy), 25, (0,255,0), cv2.FILLED)
        #extract info of each hand

    cv2.imshow("Image",img)
    if cv2.waitKey(1) == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
