import cv2
import requests
import json

def capture_photo(filename='captured_image.jpg'):
    cap = cv2.VideoCapture(0)  # 0 is the default camera

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    ret, frame = cap.read()

    # Save the captured frame as a file
    if ret:
        cv2.imwrite(filename, frame)

    cap.release()

def analyze_photo_with_asticavision(filename='captured_image.jpg'):
    API_ENDPOINT = "https://astica.ai/v1/vision"
    HEADERS = {
        "Content-Type": "application/json",
        "xi-api-key": "2F8E9B6E-147E-45E0-9AEF-1FBC719F009E74C42443-6473-4B1B-B462-791FC8EA5615"
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

def process_int(content):
    """Modified function for INT."""
    if content == "view":
        capture_photo()
        analysis_results = analyze_photo_with_asticavision()
        print(f"[interface is processed]: {analysis_results}")
    else:
        print(f"[interface is processed]: {content}")
 