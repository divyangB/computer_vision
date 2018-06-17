#!/usr/bin/python3

import cv2
import numpy as np

#   loading images
img1 = cv2.imread('drawing_1.png')
img2 = cv2.imread('drawing_2.png')

#   bitwise operations
bitwise_and = cv2.bitwise_and(img1,img2)
bitwise_or = cv2.bitwise_or(img1,img2)
bitwise_xor = cv2.bitwise_xor(img1,img2)
bitwise_not = cv2.bitwise_not(img1,img2)

#   displaying results
cv2.imshow('bitwise_and',bitwise_and)
cv2.imshow('bitwise_or',bitwise_or)
cv2.imshow('bitwise_xor',bitwise_xor)
cv2.imshow('bitwise_not',bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
