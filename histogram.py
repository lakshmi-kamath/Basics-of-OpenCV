import cv2 as cv
import numpy as np

img= cv.imread("/Users/lakshmi/U_SECTION/ML/european-shorthair-8601492_640.jpg")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
#list of images, channels,masking,histsize:no of bins, range of all values


blank=np.zeros(gray.shape[:2],dtype="uint8")
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,255,-1)
masked_hist=cv.calcHist([gray],[0],mask,[256],[0,256])
import matplotlib.pyplot as plt 

#plotting a grayscale histogram for an image 
plt.figure()
plt.title("Grayscale histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])

#plotting a masked grayscale histogram
plt.figure()
plt.title("Masked histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
plt.plot(masked_hist)
plt.xlim([0,256])
plt.show() 

#plotting a colour histogram
plt.figure()
plt.title("Coloured histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
colors=['b','g','r']
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim(0,256)
plt.show()

#plotting coloured histogram for a masked image

mask1=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,255,-1)
plt.figure()
plt.title("Masked-Coloured histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
colors=['b','g','r']
for i,col in enumerate(colors):
    hist1=cv.calcHist([img],[i],mask1,[256],[0,256])
    plt.plot(hist1,color=col)
    plt.xlim(0,256)
plt.show()

cv.waitKey(0)