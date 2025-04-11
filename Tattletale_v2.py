import numpy as np
import cv2

cap = cv2.VideoCapture("INSERT HERE")

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    roi = frame[269: 795, 537: 1416] # These numbers are what pixels in the video we 'record'.
    rows, cols, _ = roi.shape
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) # Converts roi into grayscale so that it's easier to read later
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0) # We blur the image in order to get rid of some noise

    _, threshold = cv2.threshold(gray_roi, 3, 255, cv2.THRESH_BINARY_INV) # We use this to take all the values that are the threshold between black and another color
        # We do INV on the end of the function because we want only to take in the white part
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Detecting the contours
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True) # This functions takes the contours with the biggest area to the smallest area
    
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt) # This draws a center point of the contours as a rectangle
        '''cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)''' #-1 draws all the contours
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2) # This draws a rectangle instead of the contours
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2) # This makes a line in the middle of the image, it tries to see whether our pupil is on one side or the other
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2) # Same as above just side to side
        break # This breaks the loop after the biggest contour is found
    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi) # These used to be '("Frame", frame)' but we changed it so that we only see the pixels we stated earlier.
    key = cv2.waitKey(30) # We say wait 30 milisecond between each frame
    if key == 27: #"s" key on keyboard
        break
        
cv2.destroyAllWindows() #IDK what this does im lost hehe

# Notes
# A lot of the numbers around here are specific to the one video 
# In "roi = frame"(ln10) we will have to frame each of the videos accordingly or implement a different algorithm in order to get just the eye
# I tried to get rid of typos, but can't guarantee that there are none in here
# Please upload the videos so that we can change the values accondingly
# I would recommend we make a Tattletale_v3.py where we make a lot of these things in functiosns so that we can change the values easily to test more data
# I'm pretty sure we need to automate it and everything here has to be a very manual process
# There is no way in this code to track thet changes in where the iris goes, it's only tracking where it is at any one time
