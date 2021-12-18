import cv2 as cv
import numpy as np


img = cv.imread('Photos/tower.jpg')
cv.imshow('img', img)

# AVeraging for BLUR(BLUR(BLUR(BLUR(BLUR))))
average = cv.blur(img, (3,3))
cv.imshow('Average_Blur', average)


#Gausing blue
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gauss_Blur', gauss)

#mediun blur
median = cv.medianBlur(img,3)
cv.imshow('medain_blur', median)

#bilatural  
bilatural = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral_blur', bilatural)



cv.waitKey(0)
