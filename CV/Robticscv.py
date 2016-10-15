# Standard imports
import cv2 as cv
import numpy as np
import os
#424
#425
#495
#496
#66
#67
#68
#69
#70
#71
#72
#73
#74
#75
#76
#83
#91
#92
array = []
# Read image
locate = 0
#for s in os.listdir("files"):
im = cv.imread("files/294.jpg", cv.IMREAD_COLOR)

im = cv.resize(im, (320,240))
#im = cv.bitwise_not(im)

im2 = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
cv.imshow('gray', im2)

th, im3 = cv.threshold(im2, 50, 255, cv.THRESH_BINARY);
cv.imshow('threshold', im3)

contours, hierarchy = cv.findContours(im3,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)


lan = 0
thing = 0
for c in contours:
    if(cv.contourArea(c)>0 and (((cv.contourArea(cv.convexHull(c))/cv.contourArea(c))*60)+((cv.contourArea(cv.convexHull(c)))))>=lan):
        lan = (((cv.contourArea(cv.convexHull(c))/cv.contourArea(c))*60)+((cv.contourArea(cv.convexHull(c)))))
        thing = c

(x,y),(MA,ma),angle = cv.fitEllipse(thing)
print angle
contours = [thing]

#print cv.contourArea(cv.convexHull(thing))
#print cv.contourArea(cv.convexHull(thing))/cv.contourArea(thing)*50

im4 = cv.cvtColor(im3, cv.COLOR_GRAY2BGR)
cv.drawContours(im4,contours,-1,(0,255,0),1)
#cv.imwrite("filesa/"+s, im4)
cv.imshow('title', im4)
cv.waitKey(0)
cv.destroyAllWindows()
