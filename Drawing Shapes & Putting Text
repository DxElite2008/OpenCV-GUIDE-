import cv2 as cv
import numpy as np


#this is how to make a black black image
blank = np.zeros((500, 500, 3 ), dtype="uint8")
cv.imshow('Blank', blank)
#-------------------------
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)
# 1. paint a image a certain colour

blank[200:300, 300:400] = 0, 0, 255
cv.imshow('green', blank)

# draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1 )
cv.imshow("rect", blank)

#draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('cirlce', blank)

#draw line
cv.line(blank, (100,250),(300,400), (255,255,255), thickness=3)
cv.imshow('line', blank)

#write text
cv.putText(blank, 'Hello my name is ali!!!', (50,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('text', blank)



cv.waitKey(0) 
