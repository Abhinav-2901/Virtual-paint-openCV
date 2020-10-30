import cv2
import numpy as np

frameWidth = 640
frameHeight = 240
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty(a):
    pass


# Creating Trackbar for all 6 values

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBard", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# Creating while loop

while True:
    
    _, img = cap.read()
    
    # Converting image to HSV
    
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Catching Trackbar values of all 6
    
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    
    # Creating Mask
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    
    #Get Result
    
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, result])
    
    
    
    cv2.imshow('Horizontal STacking', hstack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    
cap.release()
cv2.destroyAllWindows()