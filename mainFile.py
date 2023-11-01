import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
import allColors as CL
import blueDetect as BL
import redDetect as RD
import greenDetect as GR
import detectElse as DE
import os

GPIO.setmode(GPIO.BOARD)
inPin = 40
GPIO.setup(inPin, GPIO.IN)

def color_detection(blue_detect, red_detect, green_detect):
    if blue_detect:
        BL.do_blue()
    elif red_detect:
        RD.do_red()
    elif green_detect:
        GR.do_green()
    else:
        DE.do_else()

def contour(frame, blue_detect, red_detect, green_detect, blue_contour, red_contour, green_contour):
    if blue_detect:
        cv2.imshow("Color Detection", blue_contour)
    elif red_detect:
        cv2.imshow("Color Detection", red_contour)
    elif green_detect:
        cv2.imshow("Color Detection", green_contour)
    else:
        cv2.imshow("Color Detection", frame)
        

# Initialize the USB camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera (usually USB camera)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set the frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

inPin = 40

flag = True 

GPIO.setup(inPin, GPIO.IN)
on = GPIO.input(inPin)
os.system("espeak 'press the button to start scanning'")
while on:
    on = GPIO.input(inPin)
    if not on:
        while True:
            # Capture a frame from the camera
            ret, frame = cap.read()

            # Check if the frame was captured successfully
            if not ret:
                print("Error: Could not read frame.")
                break

            # Check if blue is detected in the frame
            blue_detected, frame_with_contours_BLUE = CL.is_blue_detected(frame)
            red_detected, frame_with_contours_RED = CL.is_red_detected(frame)
            green_detected, frame_with_contours_GREEN = CL.is_green_detected(frame)

            color_detection(blue_detected, red_detected, green_detected)

            # Display the frame with contours
            contour(frame, blue_detected, red_detected, green_detected, frame_with_contours_BLUE, frame_with_contours_RED, frame_with_contours_GREEN)

            # Exit the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                flag = False 
                break
    
        
    

    
    
cap.release()
cv2.destroyAllWindows()