def iris_detector(video="INSERT HERE", f1=269, f2=795, f3=537, f4=1416, b1=7, b2=7, thrsh=3):
    cap = cv2.VideoCapture(video)
    
    while True:
    ret, frame = cap.read()
    if ret is False:
        break
    roi = frame[f1: f2, f3: f4] # These numbers are what pixels in the video we 'record'.
    rows, cols, _ = roi.shape
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) # Converts roi into grayscale so that it's easier to read later
    gray_roi = cv2.GaussianBlur(gray_roi, (b1, b2), 0) # We blur the image in order to get rid of some noise

    _, threshold = cv2.threshold(gray_roi, thrsh, 255, cv2.THRESH_BINARY_INV) # We use this to take all the values that are the threshold between black and another color
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
        
    cv2.destroyAllWindows()
