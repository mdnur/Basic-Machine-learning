#OpenCV version 4.x Scale-Invariant Feature Transform
import cv2 #opencv-python
# Loading the image
img = cv2.imread('geeks.png')
# Converting image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Using SIFT from opencv-contrib-python
sift = cv2.SIFT_create()
# Detect keypoints and descriptors
kp, descriptors = sift.detectAndCompute(gray, None)
# Marking the keypoint on the image using circles
img = cv2.drawKeypoints(gray, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('image-with-keypoints1.jpg', img)

'''kp, descriptors = sift. detectAndCompute (gray, None)': This line uses the SIFT
detector ('sift *) to detect keypoints and compute their descriptors in the grayscale image ('gray*). 
The detected keypoints are stored in the variable 'kp', and 
their descriptors are stored in the variable 'descriptors'''

