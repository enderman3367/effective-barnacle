# Import necessary libraries
import mediapipe as mp

# Install MediaPipe
# Run this in your terminal or command prompt:
# $ python -m pip install mediapipe

# Define helper functions

def distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    dx = point1.x - point2.x
    dy = point1.y - point2.y
    dz = point1.z - point2.z
    return (dx**2 + dy**2 + dz**2)**0.5


def recognize_gesture(landmarks):
    """Recognize hand gesture based on landmarks."""
    THRESHOLD = 0.05  # Adjust this value based on your needs

    thumb_distance = distance(landmarks[4], landmarks[2])
    index_distance = distance(landmarks[8], landmarks[5])
    middle_distance = distance(landmarks[12], landmarks[9])
    ring_distance = distance(landmarks[16], landmarks[13])
    pinky_distance = distance(landmarks[20], landmarks[17])

    if thumb_distance < THRESHOLD and index_distance < THRESHOLD and middle_distance < THRESHOLD and ring_distance < THRESHOLD and pinky_distance < THRESHOLD:
        return "Rock"
    elif thumb_distance > THRESHOLD and index_distance > THRESHOLD and middle_distance > THRESHOLD and ring_distance > THRESHOLD and pinky_distance > THRESHOLD:
        return "Paper"
    elif index_distance > THRESHOLD and middle_distance > THRESHOLD and ring_distance < THRESHOLD and pinky_distance < THRESHOLD:
        return "Scissors"
    else:
        return "Unknown"

# MediaPipe setup for Hand Landmarker

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a hand landmarker instance for images
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='/Users/reddskye/ID Project/hand_landmarker.task'),
    running_mode=VisionRunningMode.IMAGE
)


# Load the image and recognize the gesture

with HandLandmarker.create_from_options(options) as landmarker:
    # Load the input image from an image file or a numpy array
    mp_image = mp.Image.create_from_file('/Users/reddskye/ID Project/captured_image.jpg')
    # Alternatively, if you have a numpy array:
    # mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=numpy_image)

    # Detect landmarks
    hand_landmarker_result = landmarker.detect(mp_image)

    # Recognize the gesture
    if hand_landmarker_result.hand_landmarks:
        landmarks = hand_landmarker_result.hand_landmarks[0]
        gesture = recognize_gesture(landmarks)
        print(gesture)
    else:
        print("No hand detected.")