#!/usr/bin/python3
# both images must be of same size
import cv2
import numpy as np
import time

img1 = cv2.imread('1.jpg',1)  #road
img2 = cv2.imread('2.jpg',1)  #car

# to remove colour of the car, further used iin removing background
img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add both the images , it just adds two images(not recommended)
sum1 = cv2.add(img1,img2)

#  to add images by deciding their intensities
weighted = cv2.addWeighted(img1,1,img2,0.4,0)

# values until 170 will be black and after that all the values will be white
#ret, mask = cv2.threshold(img2_gray,170,255,cv2.THRESH_BINARY)

#covering original car with the masked image of the car , when THRESH_Binary is used colour is black therefore INV is used
ret, mask = cv2.threshold(img2_gray,252,255,cv2.THRESH_BINARY_INV)

imgg = cv2.add(img2,img2, mask = mask)


#---------------------displaying images---------------------------------
#cv2.imshow('gray',img2_gray)
#cv2.imshow('thresh',mask)
cv2.imshow('new',imgg)
#cv2.imshow('img1',img1)
#cv2.imshow('img2',img2)
#cv2.imshow('sum',sum1)
#cv2.imshow('weighted', weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()
