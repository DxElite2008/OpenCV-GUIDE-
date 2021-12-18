import cv2 as cv

img = cv.imread('Photos/catss.jpg')
cv.imshow('catts', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
cv.imshow('grayscale', gray)


#?simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('SIMPLE_THRESH', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('INV_THRESH', thresh_inv)


#?Adaptive thresholding
adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("AdAAPTIIVE THRESHILDING", adaptive_threshold)








cv.waitKey(0)
