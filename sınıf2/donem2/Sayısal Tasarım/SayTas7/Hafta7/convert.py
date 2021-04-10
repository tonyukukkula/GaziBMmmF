import cv2
import numpy as np
frame = cv2.imread("4.png")
lower_black = np.array([0,0,0], dtype = "uint16")
upper_black = np.array([220,180,180], dtype = "uint16")
4
cv2.imshow('mask0',frame)

black_mask = cv2.inRange(frame, lower_black, upper_black)

cv2.imshow('mask0',black_mask)
cv2.imwrite("yeni4.png",black_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()