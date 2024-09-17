# Low Power Facial Detection Security System

### Description

This is a low power security system that uses facial recognition. There is a rasperry pi pico that runs off a 9V battery with a PIR motion sensor that will turn on a raspberry pi when motion is detected.

Then, with an encoding of my face generated using opencv and the face_recognition library the camera feed of the raspberry pi is scanned for faces. If my face is detected the facial_rec_mailer script terminates. Otherwise a picture of the unknown face is sent to my email.

![Final Assembly, AUG 2023](./images/IMG_2364.png "V1.0")

![Final Assembly Angle 2, AUG 2023](./images/IMG_2365.png "V1.0")