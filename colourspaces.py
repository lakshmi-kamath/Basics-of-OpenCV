import cv2 as cv


img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")

'''Colour spaces basically a space of colours, a system of representing an array of pixel colour
Colour space examples: RGB,GRAYSCALE,HSV,LAB etc.,'''

#convert from bgr to gray scale: show the distribution of pixel intensities at particular locations
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#BGR to HSV format: how humans percieve colours
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

#BGR to LAB:washed down version of BGR
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)

#the colour-format outside Open CV is RGB thus it reverses the format in matplotlib
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()
plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB)) #Converts from BGR to RGB
plt.show()

#CanNOT CONVERT GRAYSCALE TO hsv :Grayscale->BGR->HSV

#hsv to bgr
hsv_to_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)

cv.imshow("Image",hsv_to_bgr)
cv.waitKey(0)