import cv2 as cv #Import OpenCV
import numpy as np #Import Numpy (will be used later on)
import matplotlib.pyplot as plt #Import MatplotLib (mostly to display the results)

cap = cv.VideoCapture(0) #Capture with the main camera

#Loop to display capture by capture.
while (True):

    ret, frame = cap.read() #ret = check if capture was successful, frame = display matrix of the capture

    cv.imshow("Display", frame) #Display frame

    #Press q to quit (stop the loop)
    if cv.waitKey(1) == ord('q'):
        break
