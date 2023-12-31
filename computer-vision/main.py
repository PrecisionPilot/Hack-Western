import cv2
import mediapipe as mp
import pyautogui
import math
import speech_to_text
import time
from playsound import playsound

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Temporary variables
left_tmp = False
right_tmp = False
top_temp = False
bottom_temp = False
is_recording = False
recording_timer = 0

# Calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

#activating the camera
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    #detecting the face
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    #getting frame parameters
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        #detecting only the iris
        for id, landmark in enumerate(landmarks):

            #getting coordinates
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            #print(x, y)

            #setting up the mouse
            if id == 6:
                screen_x = screen_w / frame_w * x * 1.5 - (screen_w * (1 - 1 / 1.5) / 2)
                screen_y = screen_h / frame_h * y * 1.5 - (screen_h * (1 - 1 / 1.5) / 2)
                # Bount screen_x, screen_y coordinates within the limits
                screen_x = [screen_x, screen_w][screen_x > screen_w]
                screen_x = [screen_x, 0][screen_x < 0]
                screen_y = [screen_y, screen_h][screen_y > screen_h]
                screen_y = [screen_y, 0][screen_y < 0]
                #pyautogui.moveTo(x, y)
                pyautogui.moveTo(screen_x, screen_y)

        # Calculate head angle
        delta_x = landmarks[10].x - landmarks[152].x
        delta_y = landmarks[10].y - landmarks[152].y
        angle_head = math.atan(delta_x/delta_y)

        #print(angle_head)

        #moving up
        if angle_head < 0 and not top_temp:
            print("top")
            y_factor = int(angle_head * frame_h * 10)
            pyautogui.scroll(y_factor)
            pyautogui.sleep(0.5)
            top_temp = True
        if angle_head > 0:
            top_temp = False

        #moving down
        if angle_head > 0 and not bottom_temp:
            print("bottom")
            y_factor = int(angle_head * frame_h * -10)
            pyautogui.scroll(y_factor)
            pyautogui.sleep(0.5)
            bottom_temp = True
        if angle_head < 0:
            bottom_temp = False

        #moving right
        if angle_head < -0.15 and not right_tmp:
            print("right")
            x_factor = int(angle_head * frame_w  * 10)
            pyautogui.hscroll(x_factor)
        # Calculate mouth y length
        mouth_lenh = landmarks[17].y - landmarks[0].y
        mouth_lenw = landmarks[291].x - landmarks[61].x

        relative_mouth_lenh = mouth_lenh / mouth_lenw

        #print(angle_head)

        # #moving up
        # if angle_head < 0 and not top_temp:
        #     print("top")
        #     y_factor = int(angle_head * frame_h * 10)
        #     pyautogui.scroll(y_factor)
        #     pyautogui.sleep(0.5)
        #     top_temp = True
        # if angle_head > 0:
        #     top_temp = False

        # #moving down
        # if angle_head > 0 and not bottom_temp:
        #     print("bottom")
        #     y_factor = int(angle_head * frame_h * 10)
        #     pyautogui.scroll(y_factor)
        #     pyautogui.sleep(0.5)
        #     bottom_temp = True
        # if angle_head < 0:
        #     bottom_temp = False

        if relative_mouth_lenh > 1 and not is_recording:
            playsound("sound 1.mp3")
            speech_to_text.Start()
            is_recording = True
        if relative_mouth_lenh > 0.7:
            recording_timer = time.time()
        if time.time() - recording_timer > 2 and is_recording:
            playsound("sound 2.mp3")
            speech_to_text.Stop()
            pyautogui.typewrite(speech_to_text.SpeechToText())
            is_recording = False

        #moving right
        if angle_head < -0.15 and not right_tmp:
            # speech_to_text.Start()
            print("right")
            pyautogui.scroll(-400)
            pyautogui.sleep(0.5)
            right_tmp = True
        if angle_head > -0.10:
            right_tmp = False

        #moving left
        if angle_head > 0.15 and not left_tmp:
            # speech_to_text.Stop()
            # speech_to_text.SpeechToText()
            print("left")
            pyautogui.scroll(400)
            pyautogui.sleep(0.5)
            left_tmp = True
        if angle_head < 0.10:
            left_tmp = False

        # Left click
        left_eye_y = distance(landmarks[145].x, landmarks[145].y, landmarks[159].x, landmarks[159].y)
        left_eye_x = distance(landmarks[133].x, landmarks[133].y, landmarks[33].x, landmarks[33].y)
        relative_left_eye_h = left_eye_y / left_eye_x
        for landmark in [landmarks[33], landmarks[133], landmarks[145], landmarks[159]]:
            #getting coordinates
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        
        # Right click
        right_eye_y = distance(landmarks[374].x, landmarks[374].y, landmarks[386].x, landmarks[386].y)
        right_eye_x = distance(landmarks[263].x, landmarks[263].y, landmarks[362].x, landmarks[362].y)
        relative_right_eye_h = right_eye_y / right_eye_x
        for landmark in [landmarks[362], landmarks[263], landmarks[374], landmarks[386]]:
            #getting coordinates
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        # Perform click
        print(relative_right_eye_h - relative_left_eye_h)
        if relative_right_eye_h - relative_left_eye_h < -0.15:
            pyautogui.leftClick()
            pyautogui.sleep(0.5)
        elif relative_right_eye_h - relative_left_eye_h > 0.12:
            pyautogui.rightClick()
            pyautogui.sleep(0.5)


    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)

