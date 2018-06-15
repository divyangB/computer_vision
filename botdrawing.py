#!/usr/bin/python3

#loading opencv module
import cv2

#loading numpy
import numpy



#to read image in colour
img= cv2.imread('my.jpg',1)

	      #starting ,ending	,colour,width of the line
cv2.line(img,(23,118),(89,94),(0,0,187),6)


#to display colourful image
cv2.imshow('bot',img)

#to display b&w image
#cv2.imshow('grey',img1)

#to hold screen for infinite time
cv2.waitKey(0)
cv2.destroyAllWindows()
