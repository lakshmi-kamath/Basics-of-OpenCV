import cv2 as cv
import numpy as np

img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")

b,g,r=cv.split(img)
# cv.imshow("Blue",b)
# cv.imshow("Green",g)
# cv.imshow("Red",r)

print(f"img.shape={img.shape},\nBlue.shape={b.shape},\nGreen.shape={g.shape},\nRed.shape={r.shape}")
#depicted as grayscale to depict the intensity of pixels and have a shape of 1 

merged=cv.merge([b,g,r])
cv.imshow("Merged Image",merged)
blank=np.zeros(img.shape[:2],dtype='uint8') #extract the first 2 elements of the tuple

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

#reconstruct the image and show the respective colours 

cv.waitKey(0)