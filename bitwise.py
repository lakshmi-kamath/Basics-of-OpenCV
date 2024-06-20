import cv2 as cv
import numpy as np

#Bitwise operators are used in masks. 
blank=np.zeros((400,400),dtype="uint8")

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("rectanle",rectangle)
cv.imshow("Circle",circle)

bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow("AND",bitwise_and) #intersecting regions

bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow("OR",bitwise_or) #both intersecting and unique regions

bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow("XOR",bitwise_xor) #only non intersecting regions

bitwise_not=cv.bitwise_not(rectangle)
cv.imshow("NOT",bitwise_not) #inverts the image

cv.waitKey(0)