#face detection detecs the presence of a face in the image while face recognition recognises whose face it is
#face detection performed using a classifier which is an algorithm that esentialluy decides whether a given image is positive or negative,whether a face is presnt or not
#Classifier needs to be trained on lots of images with and without faces but Open CV already comes with pre trainned classifiers
#2 important classifiers: hard cascades and local binary pattern

import cv2 as cv
img=cv.imread("lady.jpeg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
bi=cv.bilateralFilter(gray,5,17,17)
#face detection does not involve skin tone. The hardcascdes look at the image and using the edges try to detect if its a face or not
hard_cascade=cv.CascadeClassifier("face_detect.xml") 
faces_recocognised=hard_cascade.detectMultiScale(bi,scaleFactor=1.29,minNeighbors=2)
print(f"Number of faces recognised :{len(faces_recocognised)}")
for (x,y,w,h) in faces_recocognised:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("Detected",img)
cv.waitKey(0)

#hardcascades are very sensitive to noise in an image and are not the most advance/precise mechanism
#delibs recogniser is better as it is less pronne to noise
#can extend to videos by dtecting frame in every frame 