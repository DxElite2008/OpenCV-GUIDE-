import cv2 as cv
import numpy as np


blank = np.zeros((400,400), dtype='uint8')


rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), (200), 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('circle', circle)


#bitwise AND(inter secting reign)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwis_and', bitwise_and)

#Bitwise  OR(non inter secting reign and inter secting reign)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise-or', bitwise_or)


#Bitwise XOR(not intersecting reign)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)


#Bitwiwse Not
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("rectangle_not", bitwise_not)

bitwise_not = cv.bitwise_not(circle)
cv.imshow("circle_not", bitwise_not)




cv.waitKey(0)

