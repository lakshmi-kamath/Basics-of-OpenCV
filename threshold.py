#Thresholding is the binarization of an image, ie., where pixels are 0/255 ie.,white
#if pixel intensity<threshold then 0 else set it to 255

import cv2 as cv
img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Simple thresholding: cv.threshold function 
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("Simple threshold",thresh)
#inverse threshold
threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("Simple threshold Inverse",thresh_inv) #sets values less than 150 to 255

#adaptive thresholding: manually specify a threshold value thus let computer find the value for threshold
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3) #mean of neighbouring picxel intensities
#gray img, max value,adaptive method,threshold type,kernel size,c value 
cv.imshow("Adaptive thresholding",adaptive_thresh)

#inverse adaptive threshold
adaptive_thresh_inv=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3) 
cv.imshow("Inverse Adaptive thresholding",adaptive_thresh_inv)

#theres gaussian method as well where it adds a weight to each pixel value and finds the mean of weights

cv.waitKey(0)