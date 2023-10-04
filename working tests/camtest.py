import cv2
import requests
import json
import base64

def capture_photo(filename='captured_image.jpg'):
    cap = cv2.VideoCapture(0)  # 0 is the default camera

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    for i in range(11):
        ret, frame = cap.read()

    # Save the 11th frame as a file
    if ret:
        cv2.imwrite(filename, frame)
        # Display the captured frame in a window
        cv2.imshow('Captured Image', frame)
        cv2.waitKey(0)  # Wait until a key is pressed
        cv2.destroyAllWindows()

    cap.release()