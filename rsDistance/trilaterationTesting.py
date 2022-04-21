
import numpy as np
import cv2
import pyrealsense2
from realsense_depth import *



dc = DepthCamera()
ret, depth_frame, color_frame = dc.get_frame()

# show image
cv2.imshow('image', color_frame)


#class for points and distances
class refPoint:
  def __init__(self, id, x, y,z,dist):
    self.id = id
    self.x = x
    self.y = y
    self.z = z
    self.coord = np.array([x,y,z])
    self.dist = dist
class intersectionPlanes:
  def __init__(self, id, nVec, c):
      self.id = id
      self.nVec = nVec
      self.c = c

    


#known points and distances, distances are variable
#calibration points
point1 = refPoint('origin',0,0,0, 10.72)
point2 = refPoint('z',0,0,400, 9.89)
point3 = refPoint('x',400,0,0, 10.29)
point4 = refPoint('y',0,400,0, 10.48)

# creating list       
keyPointsList = [] 
  
# appending instances to list 
keyPointsList.append(point1)
keyPointsList.append(point2)
keyPointsList.append(point3)
keyPointsList.append(point4)

for obj in keyPointsList:
    print(obj.coord)


#pointsEstimates list
pointsEstimates = []
#intersectionPlanes list
intPlanes = []

#recursive function?
#store intersection planes and point estimates in a list
#find intersection plane between two spheres
def intersectionPlane(p1,p2,d1,d2):
    Dvec1 = p2-p1
    DvecNorm1 = np.linalg.norm(Dvec1)
    nVec1 = Dvec1/DvecNorm1
    littled1 = (d2**2 - d1**2 - DvecNorm1**2)/((-2)*DvecNorm1)
    c1 = littled1+np.dot(nVec1,p1)
    
    return nVec1, c1


#find intersection of those three planes
def vEstimate(nVec1,nVec2,nVec3,c1,c2,c3):
    v = np.dot(np.linalg.inv(np.array([nVec1,nVec2,nVec3])),np.array([[c1],[c2],[c3]]))
    #print(v)
    return v


#define the events for the
# mouse_click.
pointer = (0,0)
px1 = (0,0)
px2 = (0,0)
px3 = (0,0)
px4 = (0,0)
d1 = 0
d2 = 0
d3 = 0
d4 = 0
state = 1
breakFlag = 0

def mouse_click(event, x, y, 
                flags, param): 
    # to check if left mouse 
    global pointer
    global px1
    global px2
    global px3
    global px4
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
    global breakFlag

    distance = depth_frame[pointer[1],pointer[0]]

    pointer = (x,y)
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_TRIPLEX
        LB = 'Left Button'
        if state ==1 :
            px1 = (x,y)
            d1 = distance
            point1.dist = distance
            state = 2
        elif state ==2:
            px2 = (x,y)
            d2 = distance
            point2.dist = distance
            state = 3
        elif state ==3:
            px3 = (x,y)
            d3 = distance
            point3.dist = distance
            state = 4
        elif state ==4:
            px4 = (x,y)
            d4 = distance
            point4.dist = distance
            state = 1
    if event == cv2.EVENT_RBUTTONDOWN:
        breakFlag = 1

    
  
cv2.setMouseCallback('image', mouse_click)


while True:
    ret, depth_frame, color_frame = dc.get_frame()
    
    cv2.circle(color_frame, pointer, 4,(0,0,255))

    cv2.circle(color_frame, px1, 4,(255,0,0))
    cv2.putText(color_frame,"{}mm".format(d1),(px1[0],px1[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    
    cv2.circle(color_frame, px2, 4,(0,255,0))
    cv2.putText(color_frame,"{}mm".format(d2),(px2[0],px2[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    
    cv2.circle(color_frame, px3, 4,(0,255,255))
    cv2.putText(color_frame,"{}mm".format(d3),(px3[0],px3[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    
    cv2.circle(color_frame, px4, 4,(255,255,0))
    cv2.putText(color_frame,"{}mm".format(d4),(px4[0],px4[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    

    if depth_frame[pointer[1],pointer[0]] != 0:
        distance = depth_frame[pointer[1],pointer[0]]
        cv2.putText(color_frame,"{}mm".format(distance),(pointer[0],pointer[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    else:
      cv2.putText(color_frame,"?",(pointer[0],pointer[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
      



    cv2.imshow("image", color_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    if breakFlag ==1:
        breakFlag = 0
        break

#compute 3 intersection planes
nVec1 = intersectionPlane(point1.coord,point2.coord,point1.dist,point2.dist)[0]
c1 = intersectionPlane(point1.coord,point2.coord,point1.dist,point2.dist)[1]
nVec2 = intersectionPlane(point2.coord,point3.coord,point2.dist,point3.dist)[0]
c2 = intersectionPlane(point2.coord,point3.coord,point2.dist,point3.dist)[1]
nVec3 = intersectionPlane(point3.coord,point4.coord,point3.dist,point4.dist)[0]
c3 = intersectionPlane(point3.coord,point4.coord,point3.dist,point4.dist)[1]

print(point1.dist)
print(point2.dist)
print(point3.dist)
print(point4.dist)
#compute final position estimate
v1 = vEstimate(nVec1,nVec2,nVec3,c1,c2,c3)
print(v1)


