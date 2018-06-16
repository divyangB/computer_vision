#!/usr/bin/python3
#history = It simply states how many previous frames are used for building the background model. So basically if an item is standing at a fixed position for as many frames as the history size, then it will disappear in the background.

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# cv2 function for bg subtraction
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25,detectShadows = True)  # in built gaussian and morphological and detecting shadows

while cap.isOpened():
	_,frame = cap.read()
	mask = subtractor.apply(frame)
	cv2.imshow("frame",frame)
	cv2.imshow("mask",mask)
	if cv2.waitKey(50) & 0xff == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
