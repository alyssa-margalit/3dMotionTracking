import cv2
import pyrealsense2
from realsense_depth import *

point = (400,300)
def show_distance(event,x,y,args,params):
    global point
    point = (x,y)
    #print(x,y)

point1 = (0,0)
point2 = (0,0)
point3 = (0,0)
state = 1

def mouse_click(event,x,y,flags,param):
    print("hi")
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_TRIPLEX
        LB = 'Left Button'
        point1 = (x,y)
        cv2.circle(color_frame, point1, 4,(255,0,0))
        print("hello")

#initialize camera
dc = DepthCamera()

#create mouse event
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)
cv2.namedWindow('img')
cv2.setMouseCallback("img", mouse_click)

while True:
    ret, depth_frame, color_frame = dc.get_frame()


    #show distance from a specific point
    
    cv2.circle(color_frame, point, 4,(0,0,255))
    if depth_frame[point[1],point[0]] != 0:
        distance = depth_frame[point[1],point[0]]
    cv2.putText(color_frame,"{}mm".format(distance),(point[0],point[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)

    #print(distance)
    cv2.imshow("Color frame", color_frame)
    cv2.imshow("img",depth_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break