import cv2 as cv
import numpy as np

def subdivide(image, subdivision, topLevel = True, singleSubdivision = False, toreturn = {}):
    height, width = image.shape  # get width and height
    dictionary = {}

    if subdivision < 0:  # default case
        return;

    # check if the subdivision works
    if (width % (2 ** subdivision) == 0) and (height % (2 ** subdivision) == 0):
        y = 0
        x = 0

        chunkX = width / (2 ** subdivision)
        chunkY = height / (2 ** subdivision)

        indexX = 0  # for dictionary
        indexY = 0

        while y in range(0, height):

            while x in range(0, width):
                # check if x or y is greater than the resolution
                if (x + chunkX <= width) and (y + chunkY <= height):

                    imgdat = {}  # reset
                    # add to dictionary

                    imgdat["boundingbox"] = (x, y), (x + chunkX, y + chunkY)
                    imgdat["boundingpercent"] = \
                        ((x / width) * 100,  (y / height) * 100),\
                        (((x + chunkX) / width * 100), ((y + chunkY) / height * 100))
                    imgdat["imgdat"] = image[y:y + chunkY, x:x + chunkX]

                    dictionary[str(indexY) + "_" + str(indexX)] = imgdat  # nest data
                    indexX += 1
                x += chunkX  # next chunk on the x-axis
            y += chunkY  # next chunk on the y-axis
            x = 0  # reset x
            indexX = 0
            indexY += 1
    else:
        raise ValueError("Subdivision " + str(subdivision) + " is too high\n\
for an image of size " + str(width) + "x" + str(height))

    if topLevel:  # loop through all subdivisions
        i = subdivision + 1
        while i > 0:  # loop through each subdivision

            # go through each subdivision adding the dictionary each time
            toreturn[i - 1] = subdivide(image, i - 1, False, False, toreturn)
            i -= 1

        return toreturn  # final dictionary

    return dictionary



img = cv.imread('img.jpg', 0)
print len(subdivide(img, 4)[1])
cv.imshow('title', subdivide(img, 4)[1]["0_0"]["imgdat"])
cv.waitKey(0)
cv.destroyAllWindows()
