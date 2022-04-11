
import numpy as np


#class for points and distances
class refPoint:
  def __init__(self, x, y,z,dist):
    self.x = x
    self.y = y
    self.z = z
    self.coord = np.array([x,y,z])
    self.dist = dist


#known points and distances, distances are variable
point1 = refPoint(0,0,0, 10.72)
point2 = refPoint(0,0,1, 9.89)
point3 = refPoint(0,1,0, 10.29)
point4 = refPoint(1,0,0, 10.48)

# creating list       
pointsList = [] 
  
# appending instances to list 
pointsList.append(point1)
pointsList.append(point2)
pointsList.append(point3)
pointsList.append(point4)

for obj in pointsList:
    print(obj.coord)



#find intersection plane between two spheres
def intersectionPlane(p1,p2,d1,d2):
    Dvec1 = p2-p1
    DvecNorm1 = np.linalg.norm(Dvec1)
    nVec1 = Dvec1/DvecNorm1
    littled1 = (d2**2 - d1**2 - DvecNorm1**2)/((-2)*DvecNorm1)
    c1 = littled1+np.dot(nVec1,p1)
    return nVec1, c1

#compute 3 intersection planes
nVec1 = intersectionPlane(point1.coord,point2.coord,point1.dist,point2.dist)[0]
c1 = intersectionPlane(point1.coord,point2.coord,point1.dist,point2.dist)[1]
nVec2 = intersectionPlane(point2.coord,point3.coord,point2.dist,point3.dist)[0]
c2 = intersectionPlane(point2.coord,point3.coord,point2.dist,point3.dist)[1]
nVec3 = intersectionPlane(point3.coord,point4.coord,point3.dist,point4.dist)[0]
c3 = intersectionPlane(point3.coord,point4.coord,point3.dist,point4.dist)[1]

#find intersection of those three planes
def vEstimate(nVec1,nVec2,nVec3,c1,c2,c3):
    v = np.dot(np.linalg.inv(np.array([nVec1,nVec2,nVec3])),np.array([[c1],[c2],[c3]]))
    #print(v)
    return v

#compute final position estimate
v1 = vEstimate(nVec1,nVec2,nVec3,c1,c2,c3)
print(v1)


