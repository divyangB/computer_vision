#!/usr/bin/python3

import cv2
import numpy as np

# reading the image as coloured using 1
img = cv2.imread('watch.jpg',1)
#converting to hsv from bgr
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# setting up the boundary of the red colour
lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])
# create a red HSV colour boundary and 
# threshold HSV image
mask = cv2.inRange(hsv,lower_red,upper_red)
#  Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img,mask)
# displaying the original image
cv2.imshow('Original',img)
# finding edges from the original
edges = cv2.Canny(img,100,200)
# displaying only the edges
cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
