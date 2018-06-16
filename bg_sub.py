#!/usr/bin/python3

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
_,first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray,(5,5),0)
#fgbg = cv2.createBackgroundSubtractorMOG()
while cap.isOpened():
	status,frame = cap.read()
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray_frame = cv2.GaussianBlur(gray_frame,(5,5),0)
	differ = cv2.absdiff(first_gray,gray_frame)
	ret , differ1= cv2.threshold(differ,25,255,cv2.THRESH_BINARY) #threshold returns two results
	#fgmask = fgbg.apply(frame)
	cv2.imshow('fr1',first_frame)
	cv2.imshow('fr',frame)
	cv2.imshow("difference",differ1)
	if cv2.waitKey(100) & 0xff == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
