

#----------------------This program is using canny method for edge detection-------------------------

#!/usr/bin/python3

import cv2
import numpy as np

# starting the camera
cap = cv2.VideoCapture(0)

# start capturing
while True:
	status,frame = cap.read()
	#converting to hsv
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#setting up a range of colour
	lower_red = np.array([30,50,50])
	upper_red = np.array([255,180,180])

	#create a red hsv colour boundary and
	#threshold hsv image
	mask = cv2.inRange(hsv,lower_red,upper_red)
	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame,mask)
	# displaying original image
	cv2.imshow('Original',frame)
	# using canny method for edge detection, finds edges in the input image and
    	# marks them in the output map edges
	edges = cv2.Canny(frame,100,200)
	# displaying edges
	cv2.imshow('edges',edges)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
