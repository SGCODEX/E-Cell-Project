import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    label_text = 'This is a Wireless Mouse'
    label_text1 = 'Use your left eye to click'
    label_text2 = 'And right eye to navigate'
    label_text3 = 'Enjoy :)'
    label_text4 = 'Press Q to Exit'
    pos_x = frame_w - 100
    pos_y = frame_h - 100
    cv2.putText(frame, label_text, (pos_x - 350, pos_y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(frame, label_text1, (pos_x - 350, pos_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(frame, label_text2, (pos_x - 350, pos_y + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(frame, label_text3, (pos_x - 350, pos_y + 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.putText(frame, label_text4, (pos_x - 80, pos_y + 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.015:
            pyautogui.click()
            print("Clicked")
            pyautogui.sleep(2)
        print("distance is:",left[0].y - left[1].y)
    cv2.imshow('Eye Controlled Mouse', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()