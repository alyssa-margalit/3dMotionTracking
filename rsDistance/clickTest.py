import cv2
import pyrealsense2
from realsense_depth import *



dc = DepthCamera()
ret, depth_frame, color_frame = dc.get_frame()
  
# show image
cv2.imshow('image', color_frame)
   

    

#define the events for the
# mouse_click.
pointer = (0,0)
point1 = (0,0)
point2 = (0,0)
point3 = (0,0)
point4 = (0,0)
d1 = 0
d2 = 0
d3 = 0
d4 = 0
state = 1

def mouse_click(event, x, y, 
                flags, param): 
    # to check if left mouse 
    global pointer
    global point1
    global point2
    global point3
    global point4
    global state
    global d1
    global d2
    global d3
    global d4
    global distance

    distance = depth_frame[pointer[1],pointer[0]]

    pointer = (x,y)
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_TRIPLEX
        LB = 'Left Button'
        if state ==1 :
            point1 = (x,y)
            d1 = distance
            state = 2
        elif state ==2:
            point2 = (x,y)
            d2 = distance
            state = 3
        elif state ==3:
            point3 = (x,y)
            d3 = distance
            state = 4
        elif state ==4:
            point4 = (x,y)
            d4 = distance
            state = 5
        elif state ==5:
            state = 1

    
  
cv2.setMouseCallback('image', mouse_click)
   
while True:
    ret, depth_frame, color_frame = dc.get_frame()
    
    cv2.circle(color_frame, pointer, 4,(0,0,255))

    cv2.circle(color_frame, point1, 4,(255,0,0))
    cv2.putText(color_frame,"{}mm".format(d1),(point1[0],point1[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    
    cv2.circle(color_frame, point2, 4,(0,255,0))
    cv2.putText(color_frame,"{}mm".format(d2),(point2[0],point2[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    
    cv2.circle(color_frame, point3, 4,(0,255,255))
    cv2.putText(color_frame,"{}mm".format(d3),(point3[0],point3[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    
    cv2.circle(color_frame, point4, 4,(255,255,0))
    cv2.putText(color_frame,"{}mm".format(d4),(point4[0],point4[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    

    if depth_frame[pointer[1],pointer[0]] != 0:
        distance = depth_frame[pointer[1],pointer[0]]
        cv2.putText(color_frame,"{}mm".format(distance),(pointer[0],pointer[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    else:
      cv2.putText(color_frame,"?",(pointer[0],pointer[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
      



    cv2.imshow("image", color_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
  
# close all the opened windows.
cv2.destroyAllWindows()