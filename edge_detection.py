import cv2 as cv
import numpy as np
img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#from a programming perspective we can consider edge and gradient to be the same but are mathematically different

#laplacian method 
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap)) #CONVERSOION TO IMAGE SPECIFIC DATA TYPE: positive/negative slope converted to image absolute datatype that is converted to UI8 datatype
cv.imshow("Laplacian",lap)

#Sobel gradient magnitude computatoons: computes gradients in 2 directions the x and the Y 
sobel_x=cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobel_x,sobel_y)
cv.imshow("Combined sobel",combined_sobel)

#canny edge detector: multi stage process uses sobel in one of teh stages to find the gradiant
canny=cv.Canny(gray,150,175) #threshold vcalues 
cv.imshow("Canny image",canny)
cv.waitKey(0)