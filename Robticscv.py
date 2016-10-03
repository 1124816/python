# Standard imports
import cv2 as cv
import numpy as np;

# Read image
im = cv.imread("files/205.jpg", cv.IMREAD_COLOR)

#im = cv.bitwise_not(im)

im2 = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

th, im3 = cv.threshold(im2, 100, 255, cv.THRESH_BINARY);

contours, hierarchy = cv.findContours(im3,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

lan = 0
thing = 0
for c in contours:
    if(cv.contourArea(cv.convexHull(c))>=lan):
        lan = cv.contourArea(cv.convexHull(c))
        thing = c

contours = [thing]


im4 = cv.cvtColor(im3, cv.COLOR_GRAY2BGR)
cv.drawContours(im4,contours,-1,(0,255,0),1)
cv.imshow("Keypoints", im4)
cv.waitKey(0)
