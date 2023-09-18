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

def analyze_photo_with_asticavision(filename='captured_image.jpg'):
    API_ENDPOINT = "https://astica.ai/v1/vision"
    HEADERS = {
        "Content-Type": "application/json",
        "xi-api-key": "YOUR_ASTICA_API_KEY"
    }
    
    with open(filename, 'rb') as file:
        encoded_image = base64.b64encode(file.read()).decode('utf-8')
    
    payload = {
        "image": encoded_image,
        "model": "1.0_full",  # You can change this to "2.0_full" if needed
        "features": "all"  # You can specify specific features if needed
    }
    
    response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API returned {response.status_code}: {response.text}"}