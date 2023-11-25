import cv2
import mediapipe as mp
import pyautogui
import math

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Temporary variables
left_tmp = False
right_tmp = False
top_temp = False
bottom_temp = False

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
            pyautogui.sleep(0.5)
            right_tmp = True
        if angle_head > -0.15:
            right_tmp = False

        #moving left
        if angle_head > 0.15 and not left_tmp:
            print("left")
            x_factor = int(angle_head * frame_w  * -10)
            pyautogui.hscroll(x_factor)
            pyautogui.sleep(0.5)
            left_tmp = True
        if angle_head < 0.15:
            left_tmp = False

        #clicking functionality
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            #getting coordinates
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        if(left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)


    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)

