import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/pexels-yugandhar-bonde-3680131.jpg")
cv.imshow("img", img)

# plt.imshow(img)
# plt.show()


#BGR to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#brg to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# plt.imshow(rgb)
# plt.show()

#hsv to bgr vice vorsa for lab just change hsv to lab
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsvtobgr', hsv_bgr)













cv.waitKey(0)
