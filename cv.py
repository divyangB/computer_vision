#!/usr/bin/python3

#sudo pip3 install opencv-contrib-python

#This program is stating how to load an image in different modes and how to close it properly.

import cv2
img = cv2.imread('my.jpg',1)     #reading image in colour mode/colourful


#img1 = cv2.imread('my.jpg',0)    # 0 for removing all colours/greyscale

#img[0][0]    check colour at pixel position

#img1 = img[0:200,0:300]

cv2.imshow('adhoc',img)    #adhoc is the name of the image
    #here image can be closed by pressing any key




#cv2.rectangle(img,(100,100),(300,300),(0,0,76),5)
cv2.circle(img,(200,200),(100),(0,255,0),-1)
	#   name   center rad    color   width

#   polygon     eclipse   text       


cv2.imwrite('my1.jpg',img)      #########   to save the image locally



cv2.imshow('windowsname',img)		#_____________-to display the image
cv2.waitKey(0)    # 0 for waiting lifetime action/ infinite time
#cv2.waitKey(time)  waiting time in ms

cv2.destroyAllWindows()   #to close all windows properly
