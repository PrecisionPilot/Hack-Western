import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

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
        for landmark in landmarks[474:478]:

            #getting coordinates
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            print(x, y)

            #setting up the mouse
            # if id == 1:
            #     pyautogui.move(x, y)


    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)

