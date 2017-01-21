import cv2 as cv
import numpy as np
import matplotlib.pyplot as mpl

cap = cv.VideoCapture("greentraining.avi")

#img = cv.imread('img.jpg', 0)

#cv.imshow('title', img)
#cv.waitKey(0)
#cv.destroyAllWindows()

#cv.imwrite('chart.png', img)

while True:
    bol, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    cv.waitKey(0)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
