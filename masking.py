#masking helps us to focus on certain parts of the image only 
import cv2 as cv
import numpy as np

img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")

blank=np.zeros(img.shape[:2],dtype="uint8")
mask=cv.circle(blank,(img.shape[1]//2+45,img.shape[0]//2+45),200,255,-1)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked Image",masked)

cv.waitKey(0)