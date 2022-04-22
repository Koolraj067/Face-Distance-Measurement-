import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
textList = ["Face Distance Measurement","Project",
            "Created By : ABHISHEK RAJ",
            "Employee ID : GBSOFT-INT175"]

while True :

    success, img = cap.read()
    imgText = np.zeros_like(img)
    img, faces = detector.findFaceMesh(img,draw=False)

    if faces:
        face = faces[0]
        PointLeft = face[145]
        PointRight = face[374]
        w, _ = detector.findDistance(PointLeft,PointRight)
        W = 6.3


        # Finding the distance
        f = 840
        d = (W*f)/w
        print(d)
        cvzone.putTextRect(img, f'Distance: {int(d)}cm',(face[10][0] - 100, face[10][1] - 50), scale=2)
        for i, text in enumerate(textList):
            singleHeight = int(20 + d/5)
            scale = 0.4 + d/100
            cv2.putText(imgText, text, (50, 50 + (i * singleHeight)),cv2.FONT_ITALIC, scale, (255, 255, 255), 2)


    imgStacked = cvzone.stackImages([img,imgText],2,1)


    cv2.imshow("Image", imgStacked)

    cv2.waitKey(1)