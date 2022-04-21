import cv2
import numpy as np

img = cv2.imread('images/testImage.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cap = cv2.VideoCapture(0)

#features
orb = cv2.ORB_create()
kp_image,desc_image = orb.detectAndCompute(img,None)
img = cv2.drawKeypoints(img,kp_image,img)


while True:
    _, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #train image
    
    kp_grayframe, desc_grayframe = orb.detectAndCompute(grayframe,None)
    grayframe = cv2.drawKeypoints(grayframe, kp_grayframe, grayframe)


    cv2.imshow("Image",img)
    cv2.imshow("grayFrame",grayframe)

    key = cv2.waitKey(1)
    if key ==27:
        break

cap.release()
cv2.destroyAllWindows()