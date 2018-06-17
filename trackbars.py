#!/usr/bin/python3

import cv2
import numpy as np


def nothing(x):	
	pass

cap = cv2.VideoCapture(0)
# creating a window where we want to use trackbar
cv2.namedWindow('frame')

# creating trackbars
cv2.createTrackbar('test','frame',50,500,nothing)
cv2.createTrackbar('color/gray','frame', 0,2,nothing)

# for showing some use of the trackbar we have to keep it in the loop

while True:
	_,frame = cap.read()
	# getting the position of the trackbar
	test = cv2.getTrackbarPos('test','frame')
	font = cv2.FONT_HERSHEY_COMPLEX
	#	[ screen_position(50,150)(left,top) ]
	cv2.putText(frame, str(test), (50,150),font, 4, (0,0,255))
	#------------------- trackbar for gray colour-----------------
	s = cv2.getTrackbarPos('color/gray','frame')
	if s==0:
		pass
	elif s==1:
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	else:
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.putText(frame, str(s), (100,350),font, 4, (255,0,255))
	cv2.imshow('frame',frame)
	if cv2.waitKey(27) & 0xff == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
