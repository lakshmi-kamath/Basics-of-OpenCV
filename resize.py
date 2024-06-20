#Reize an image
import cv2 as cv
img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")
def resize(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

cv.imshow("Cat",resize(img))
cv.waitKey(0)

def changeresolution(width,height):  #only for live videos
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture(0)  #0 for web-cam
while True: 
    isTrue,frame=capture.read()
    cv.imshow("Video",resize(frame))
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

