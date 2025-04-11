
import cv2
import numpy as np

#chanti's part - ditto on the lost hehe
cap = cv2.VideoCapture("eye_recording.flv")

while True:
  ret, frame = cap.read()
  
  
  roi = frame[269: 795, 537: 1416]
  gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
  
  cv2.imshow ("gray_roi", gray_roi)
  cv2.imshow("Roi", frame)
  key = cv2.waitKey(30)
  if key == 27:
    break

cv2.destroyAllWindows()

#Contour Code (I'm a bit lost hehe)

_, _, contour, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv.2CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)

#Period !