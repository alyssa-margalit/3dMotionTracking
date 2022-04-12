import cv2
import pyrealsense2
from realsense_depth import *

  
# read image
img = cv2.imread('testImage.jpg')

dc = DepthCamera()
ret, depth_frame, color_frame = dc.get_frame()
  
# show image
cv2.imshow('image', color_frame)
   
#define the events for the
# mouse_click.
point1 = (0,0)
point2 = (0,0)
point3 = (0,0)
state = 1

def mouse_click(event, x, y, 
                flags, param): 
    # to check if left mouse 
    global point1
    global point2
    global point3
    global state

    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_TRIPLEX
        LB = 'Left Button'
        if state ==1 :
            point1 = (x,y)
            state = 2
        elif state ==2:
            point2 = (x,y)
            state = 3
        elif state ==3:
            point3 = (x,y)
            state = 1

    
  
cv2.setMouseCallback('image', mouse_click)
   
while True:
    ret, depth_frame, color_frame = dc.get_frame()
    
    cv2.circle(color_frame, point1, 4,(255,0,0))
    cv2.circle(color_frame, point2, 4,(0,255,0))
    cv2.circle(color_frame, point3, 4,(0,255,255))


    #show distance from a specific point
    
    #cv2.circle(color_frame, point, 4,(0,0,255))
    #if depth_frame[point[1],point[0]] != 0:
       # distance = depth_frame[point[1],point[0]]
    #cv2.putText(color_frame,"{}mm".format(distance),(point[0],point[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)

    #print(distance)
    cv2.imshow("image", color_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
  
# close all the opened windows.
cv2.destroyAllWindows()