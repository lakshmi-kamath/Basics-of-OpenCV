import cv2 as cv
import numpy as np

img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")

cv.imshow("Image",img)

def translate(img,x,y ):
    transMat=np.float32([[1,0,x],[1,0,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions) 

translated=translate(img,-10,-50)
cv.imshow("Translated",translated)

#Rotations ->can specify the point/ corner along which you want to rotate 

def rotate(img, angle,rotationpoint=None):
    (height,width)=img.shape[:2]
    if rotationpoint is None:
        rotationpoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotationpoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,45)
cv.imshow("Rotation",rotated)
cv.waitKey(0)

#resize the image 
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)
cv.waitKey(0)

#Flipping an image
#0->vertically , 1->>horizontally, -1 ->>both
flip=cv.flip(img,1)
cv.imshow("Flip",flip)
cv.waitKey(0) 

#crop
cropped=img[300:400,300:500]
cv.imshow("Cropped",cropped)
cv.waitKey(0)