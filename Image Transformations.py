import cv2 as cv
import numpy as np

img = cv.imread("Photos\pexels-jiarong-deng-1034662.jpg")

cv.imshow('cat', img)

#translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x ---> left
#-y ---> up
#x --->RIght
#y --->Down

translated = translate(img, -100, 100)
cv.imshow("translatred", translated)

#rotation

def rotate(img, angle, rotPoint=None):
    (hieght, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, hieght//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,hieght)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -90)
cv.imshow("Rotated_Rotated", rotated_rotated)


#resizing

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#flipping
flip = cv.flip(img, 1)
cv.imshow('fliped', flip)

#crooping
cropped = img[200:400, 400:500]
cv.imshow('cropped', cropped)



cv.waitKey(0)
