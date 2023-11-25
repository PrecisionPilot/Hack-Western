import cv2
import pyautogui

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Load the pre-trained face and eye cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Extract the region of interest (ROI) for eyes
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            # Draw rectangles around the eyes
            cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)

            # Calculate the midpoint of the eyes
            eye_midpoint_x = x + ex + ew // 2
            eye_midpoint_y = y + ey + eh // 2

            # Move the mouse based on eye gaze
            
            screen_width, screen_height = pyautogui.size()
            destination_x = int((eye_midpoint_x / frame.shape[1]) * screen_width)
            destination_y = int((eye_midpoint_y / frame.shape[0]) * screen_height)

            pyautogui.FAILSAFE = False
            pyautogui.moveTo(destination_x, destination_y, duration=0.25)

    # Display the frame
    cv2.imshow("Eye Tracking", frame)

