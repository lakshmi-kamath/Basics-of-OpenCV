#noise is caused from camera sensors or peoblems in lighting which can be reduced by blurring
import cv2 as cv

img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")

#kernel : is the window youndraw over an image, kernel size is the number of rows and  columns
#blurr is applied to the middle pixel as a result of the surrounding pixels

#averaging: define a window over a specific portion of an image which computes the pixel intensity of the middle pixel of the true centre as the average of surrounding pixel intensity 

average=cv.blur(img,(3,3)) #higher kernel size->more blurr
cv.imshow("Average bblur",average)


#Gausian Blurr: Each surrounding pixel is given a particular weight.The average of the products of those weights gives you the true centre
#less blurring than average blurr but more natural

Gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian Blurr",Gauss)

#Median Blurr: find the median of the surrounding pixels of a particular pixel
#more effective than average/Gaussian Blurring method for reducing noise 
Median=cv.medianBlur(img,3)#assumes it is 3X3 based on 3 , not for high kernel sizes
cv.imshow("Median Blurr",Median)

#Bilateral : most effective due to its blurring method, applies blurring but retains the image
bi=cv.bilateralFilter(img,5,15,15) #large values tend to make it look like median blurr
cv.imshow("Bilateral Blurr",bi)
cv.waitKey(0)