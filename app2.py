import math
import cv2
import mediapipe as mp

import pyautogui

# from scipy.signal import savgol_filter
import numpy as np

pyautogui.PAUSE = 0.001

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

threshold_grab = 0.08
bool_grab = False


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

        if handedness.classification[0].label == 'Left':
            mouse_coords = np.array([hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x, hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y, hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z])

            pyautogui.moveTo(1920 - hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * 1920, hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * 1080)
        
        click_dist = math.dist([hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x,
                                hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y], 
                                [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                                hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y])
        if handedness.classification[0].label == 'Right':
            print(click_dist, handedness.classification[0].label)
            if click_dist != None and click_dist < threshold_grab:
                bool_grab = True
                pyautogui.press('g')
            if bool_grab and click_dist > threshold_grab:
                bool_grab = False
                pyautogui.leftClick()
        if handedness.classification[0].label == 'Left':
            print(click_dist, handedness.classification[0].label)
            if click_dist != None and click_dist < threshold_grab:
                pyautogui.leftClick()

    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
