#Countours are basically the boundaries of objects,the line or curve that joins the continuous points along the boundary of the object
#Mathematically countour and edges are 2 different things
#used in shape analysis annd object detection

import cv2 as cv


img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")
cv.imshow("Image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

canny=cv.Canny(blur,125,175)
cv.imshow("Canny Edges",canny)

'''Find contour function which returns 2 values contours and hierarchy
cv.RETR_TREE-->>Hierarchical contours/cv.RETR_EXTERNAL-->>external contours
Contour approximation method cv.CHAIN_APPROX_NONE-->>does nothing returns all the contours, CHAIN_APPROX_SIMPLE--> COMPRESES ALL CONTOURS INTO SIMPLE ONES WHICH MAKE MORE SENSE
    Example: if we have a straight line, then none gives a list of all points on the line while simple takes all the points and compresses it into the end points only
cv.contour looks after the structuring element/edges of a found image and return to values the contours whichis a python list of all the contours found in the image 
hierarchies is the hierarchical representation of contour 
    Example: if we have a rectangle and a square inside it and a circle inside it then it is the hierarchy c.contour finds the contours'''



contours,hierarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')
'''Blurred images have less edges and thus less contours'''



'''Threshhold is another method to find contours where (threshhold value,mkax value)
This looks at an image and tries to binarise that image.Thus intensity of any pixel below 125 is set to 0,else it is set to white or 255'''
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Threshhold",thresh)
ontours,hierarchy=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found using threshhold')

"We can visualize the image using the contours by drawing over the image "

import numpy as np
blank=np.zeros(img.shape,dtype='uint8')

#-1: for all contours, (0,0,255): colour, 2:thickness
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Contours drawn',blank)

cv.waitKey(0)