# HumanFactor_Project

To run, first install package 
``` pip install opencv-python```
``` pip install mediapipe ```

``` ----------------------------------------------------------------- ```
STILL NOT COMPLETE, NEED MORE TRAINING DATA
How to run Face Recognition:
```cd FaceRecog
python3 face_train.py
python3 FaceRecognitionMin.py```

``` ----------------------------------------------------------------- ````
DEMO WORK SPAMPLE FOR MOTION DETECTION
python3 driver.py



``` ------------------------------------------------------------------ ```y


What we're planning so far:
-  REact for frontend, Python3 for back-end, MySQL for database
- Home page would have 2 cameras - at porch and door 
-  2 cameras, one detects motion within the porch range, one do face detection, using Mediapipe Holistic API solution
    -  For motion detection, we screenshot any unusal behavior, send notifcation to the app(can turn on/off) save it in database, data attributes(or cols whatever) with timestamp, PhotoId, img url(or something a phone can open/zoom). 
        - If we can capture the face(depends if the module can capture it), save it to database as well.
    -  For face detection, if camera detects a resident's face, send notification to the app(can turn on/off) save it in database with timestamp, photoId, resident's name.
        -  If camera detects a stranger, send notifcation to the app, save it in the database with attributes: timestamp, photoId, img url(or something a phone can open/zoom).

