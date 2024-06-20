import cv2 as cv
img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")

#Converting to gray scale
grey= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grey",grey)


#blurr an image 
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)


#Edge Cascade
canny=cv.Canny(img,175,200)
cv.imshow("canny",canny)


#dilating the image 
'''Dilation is a morphological operation in image processing that is used to enlarge the boundaries of regions of 
foreground pixels (usually white pixels) in an image. It works by placing a structuring element over the image 
and expanding the regions where the structuring element overlaps with the foreground.'''
dilate=cv.dilate(canny,(3,3),iterations=1)
cv.imshow("dilate",dilate)


#Erode an image
eroded=cv.erode(dilate,(3,3),iterations=1)
cv.imshow("eroded",eroded)


#resize and crop an image 
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#ignores the aspect ratio interpolation in background 
#smaller image INTER_AREA
#larger image INTER_LINEAR or INTER_CUBIC(slowest but better quality)
cv.imshow("Resized",resized)



#cropping based on the fact that images are arrays and thus use slicing
crop= img[50:200,50:200]
cv.imshow("Cropped",crop)
cv.waitKey(0)
