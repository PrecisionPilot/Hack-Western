import cv2
import mediapipe as mp
import pyautogui
import math
import speech_to_text

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Temporary variables
left_tmp = False
right_tmp = False

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
            if id == 1:
                screen_x = screen_w / screen_w * x
                screen_y = screen_h / screen_h * y
                #pyautogui.moveTo(x, y)
                pyautogui.moveTo(screen_x, screen_y)

        # Calculate head angle
        delta_x = landmarks[10].x - landmarks[152].x
        delta_y = landmarks[10].y - landmarks[152].y
        angle_head = math.atan(delta_x/delta_y)

        if angle_head < -0.15 and not right_tmp:
            speech_to_text.Start()
            # pyautogui.press("nexttrack")
            print("right")
            right_tmp = True
        if angle_head > -0.10:
            right_tmp = False

        if angle_head > 0.15 and not left_tmp:
            speech_to_text.Stop()
            # pyautogui.press("prevtrack")
            speech_to_text.SpeechToText()
            print("left")
            left_tmp = True
        if angle_head < 0.10:
            left_tmp = False

        #clicking functionality
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            #getting coordinates
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        if(left[0].y - left[1].y) < 0.004:
            print('click')


    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)

