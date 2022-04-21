import cv2
import numpy as np

img1 = cv2.imread("images/corner1.jpg",cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (640, 640))

img2 = cv2.imread("images/testImage.jpg",cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (640, 640))



orb = cv2.ORB_create()
#nfeatures = 20

keypoints1, descriptors1 = orb.detectAndCompute(img1,None)
keypoints2, descriptors2 = orb.detectAndCompute(img2,None)
#print(keypoints1[1])

matcher = cv2.BFMatcher()
matches = matcher.match(descriptors1,descriptors2)

final_img = cv2.drawMatches(img1,keypoints1,img2,keypoints2,matches[:20],None)

pts = np.asarray([[p.pt[0], p.pt[1]] for p in keypoints1])
print(pts[0])

#img1 = cv2.drawKeypoints(img1,keypoints,None)

cv2.imshow("Matches",final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#if limiting features, remember to mask into a couple different regions so not everything is in a little tiny area