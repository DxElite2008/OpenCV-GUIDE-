import cv2 as cv
import numpy as np


img = cv.imread('Photos/catss.jpg')
cv.imshow('cats', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", gray)

#? Laplaction 
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

#? Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx ,sobely)
cv.imshow('combined_sobel', combine_sobel)


cv.imshow("X_Sobel", sobelx)
cv.imshow('Sobel Y', sobely)


canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)





cv.waitKey(0)
