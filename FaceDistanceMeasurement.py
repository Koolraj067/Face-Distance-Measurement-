import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True :

    success, img = cap.read()
    img, faces = detector.findFaceMesh(img,draw=False)

    if faces:
        face = faces[0]
        PointLeft = face[145]
        PointRight = face[374]
        cv2.circle(img,PointLeft,5,(0,0,255),cv2.FILLED)
        cv2.circle(img, PointRight,5,(255,0,0),cv2.FILLED)
        cv2.line(img,PointLeft,PointRight,(0,255,0),1)
        w, _ = detector.findDistance(PointLeft,PointRight)
        W = 6.3 #for male it is 64mm and for female it is 62mm so avg will be 63mm

        #Finding focal length
        #d = 50
        #f = (w*d)/W
        #print(f)

        # Finding the distance
        f = 840
        d = (W*f)/w
        print(d)
        cvzone.putTextRect(img, f'Distance: {int(d)}cm',(face[10][0] - 100, face[10][1] - 50), scale=2)



    cv2.imshow("Image", img)
    cv2.waitKey(1)
