import cv2 as cv
import numpy as np

cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")
blank=np.zeros((500,500,3),dtype="uint8")
# blank[200:300]=0,255,0
# blank[300:400]=255,0,0

#Draw a rectangle with borders only
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)

# Draw a rectangle with filled in colours thickness=cv.FILLED or -1

#Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)

#Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=5)

#Write text on image
cv.putText(blank,"Hello,How are you doing?",(255,255),cv.FONT_HERSHEY_PLAIN,1.0,(255,234,0),2)

cv.imshow("Green",blank)
cv.waitKey(0)