
import numpy as np
import cv2
from combinations import *

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
  def __init__(self, nVec, c):
      #self.id = id
      self.nVec = nVec
      self.c = c
class estPoints:
  def __init__(self, id, x, y,z):
      self.id = id
      self.x = x
      self.y = y
      self.z = z

#known points and distances, distances are variable
#calibration points
point1 = refPoint(1,0,0,0, 10.72)
point2 = refPoint(2,0,0,1, 9.89)
point3 = refPoint(3,2,0,0, 10.29)
point4 = refPoint(4,0,1,0, 10.48)

# creating list       
keyPointsList = [] 
#pointsEstimates list
pointsEstimates = []
#intPlanes np array
intPlanesNP = np.empty([20,20],dtype = intersectionPlanes)
#print(intPlanesNP[0][1])
  
# appending instances to list 
keyPointsList.append(point1)
keyPointsList.append(point2)
keyPointsList.append(point3)
keyPointsList.append(point4)

for obj in keyPointsList:
    print(obj.coord)


#store intersection planes and point estimates in a list
#find intersection plane between two spheres
def intersectionPlane(p1,p2):
    Dvec = p2.coord-p1.coord
    DvecNorm = np.linalg.norm(Dvec)
    nVec = Dvec/DvecNorm
    littled = (p2.dist**2 - p1.dist**2 - DvecNorm**2)/((-2)*DvecNorm)
    c = littled+np.dot(nVec,p1.coord)
    intPlanesNP[p1.id][p2.id]=intersectionPlanes(nVec,c)
#find intersection of those three planes
def vEstimate(plane1,plane2,plane3):
    v = np.dot(np.linalg.inv(np.array([plane1.nVec,plane2.nVec,plane3.nVec])),np.array([[plane1.c],[plane2.c],[plane3.c]]))
    pointsEstimates.append(v)
    #print(v)
    return v

def intersectionPlaneExecute():
    #send all combinations of 2 points from keyPointsList to intersectionPlane function
    print("points")

def vEstimateCombine(intPlanesNP):
    #send all combinations of 3 planes from intPlanesNP to vEstimate
    #this:  https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/
    print("combine")

#questions: how far in the past should i remember? or do I just dump points and get new ones continuously


def printCombination(arr, n, r): 
      
    # A temporary array to  
    # store all combination 
    # one by one 
    data = [0]*r; 
  
    # Print all combination  
    # using temprary array 'data[]' 
    combinationUtil(arr, data, 0,  
                    n - 1, 0, r); 
  
# arr[] ---> Input Array 
# data[] ---> Temporary array to 
#         store current combination 
# start & end ---> Staring and Ending 
#             indexes in arr[] 
# index ---> Current index in data[] 
# r ---> Size of a combination  
# to be printed  
def combinationUtil(arr, data, start,  
                    end, index, r): 
                          
    # Current combination is ready  
    # to be printed, print it 
    if (index == r): 
        for j in range(r): 
            print(data[j].id, end = " "); 
        intersectionPlane(data[0],data[1])

        print(); 
        return; 
  
    # replace index with all 
    # possible elements. The 
    # condition "end-i+1 >=  
    # r-index" makes sure that  
    # including one element at 
    # index will make a combination  
    # with remaining elements at  
    # remaining positions 
    i = start;  
    while(i <= end and end - i + 1 >= r - index): 
        data[index] = arr[i]; 
        combinationUtil(arr, data, i + 1,  
                        end, index + 1, r); 
        i += 1; 
  
# Driver Code 
arr = keyPointsList
r = 2; 
n = len(arr); 
printCombination(arr, n, r)

v1 = vEstimate(intPlanesNP[1][2],intPlanesNP[2][3],intPlanesNP[3][4])
print(v1)