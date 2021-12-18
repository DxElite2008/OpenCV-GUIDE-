import cv2 as cv

img = cv.imread("Photos/pexels-ihsan-adityawarman-1056251.jpg")

cv.imshow("IMG", img)


#convert a image ot greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey', grey) 

#blur

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascade
canny = cv.Canny(img, 101, 101)
cv.imshow('canny', canny)

#dilating the image

dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)


#roading
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('crooped', cropped)


cv.waitKey(0)
