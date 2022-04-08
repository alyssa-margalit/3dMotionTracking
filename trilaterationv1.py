
import numpy as np

p1 = np.array([0,0,0])
p2 = np.array([0,0,1])
p3 = np.array([0,1,0])
p4 = np.array([1,0,0])

d1 = 10.72
d2 = 9.89
d3 = 10.29
d4 = 10.48

Dvec1 = p2-p1
#print(Dvec1)

DvecNorm1 = np.linalg.norm(Dvec1)
#print(DvecNorm1)

nVec1 = Dvec1/DvecNorm1

littled1 = (d2**2 - d1**2 - DvecNorm1**2)/((-2)*DvecNorm1)
#print(littled1)

c1 = littled1+np.dot(nVec1,p1)
#print(c1)

########## plane2

Dvec2 = p3-p2
#print(Dvec1)

DvecNorm2 = np.linalg.norm(Dvec2)
#print(DvecNorm1)

nVec2 = Dvec2/DvecNorm2

littled2 = (d3**2 - d2**2 - DvecNorm2**2)/((-2)*DvecNorm2)
#print(littled1)

c2 = littled2+np.dot(nVec2,p2)
#print(c1)

########## plane3

Dvec3 = p4-p3
#print(Dvec1)

DvecNorm3 = np.linalg.norm(Dvec3)
#print(DvecNorm1)

nVec3 = Dvec3/DvecNorm3

littled3 = (d4**2 - d3**2 - DvecNorm3**2)/((-2)*DvecNorm3)
#print(littled1)

c3 = littled3+np.dot(nVec3,p3)
#print(c1)


def intersectionPlane(p1,p2,d1,d2):
    Dvec1 = p2-p1
    #print(Dvec1)
    DvecNorm1 = np.linalg.norm(Dvec1)
    #print(DvecNorm1)
    nVec1 = Dvec1/DvecNorm1

    littled1 = (d2**2 - d1**2 - DvecNorm1**2)/((-2)*DvecNorm1)
    #print(littled1)

    c1 = littled1+np.dot(nVec1,p1)
    #print(c1)
    print("hi")

def vEstimate(nVec1,nVec2,nVec3,c1,c2,c3):
    v = np.dot(np.linalg.inv(np.array([nVec1,nVec2,nVec3])),np.array([[c1],[c2],[c3]]))
    #print(v)
    return v


v1 = vEstimate(nVec1,nVec2,nVec3,c1,c2,c3)
print(v1)
  



#v = np.dot(np.linalg.inv(np.array([nVec1,nVec2,nVec3])),np.array([[c1],[c2],[c3]]))
#print(v)

