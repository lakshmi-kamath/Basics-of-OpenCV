#Reading an image  
# import cv2 as cv
# img=cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")
# cv.imshow("Cat",img)
# cv.waitKey(0)

# Reading a Video
import cv2 as cv
capture=cv.VideoCapture(0)  #0 for web-cam
while True: 
    isTrue,frame=capture.read()
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()