import math
import cv2
import mediapipe as mp
# import time

# from one_euro_filter import OneEuroFilter
# from scipy.signal import savgol_filter

# filters = []
# for i in range(21):
#     filters.append(([0] * 100, [0] * 100))

# # The filtered signal
# min_cutoff = 0.004
# beta = 0.7
# time_frame = 0
# filters = []
# for i in range(21):
#     filters.append((OneEuroFilter(0, .0, min_cutoff=min_cutoff, beta=beta), OneEuroFilter(0, .0, min_cutoff=min_cutoff, beta=beta)))

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Text output
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = -.5
color = (255, 255, 255)
thickness = 2

# plt = None


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
        image = cv2.resize(image, (1280, 960))
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        point_index_left, point_index_right = None, None
        if results.multi_hand_landmarks:
            # time_frame += time.time()
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                print(hand_landmarks.landmark[0].x)
                for i in range(21):
                    # # savgol
                    # filters[i][0].pop(0)
                    # filters[i][0].append(hand_landmarks.landmark[i].x * 640)
                    # filtered_x = savgol_filter(filters[i][0], 11, 4)
                    # filters[i][1].pop(0)
                    # filters[i][1].append(hand_landmarks.landmark[i].y * 480)
                    # filtered_y = savgol_filter(filters[i][1], 11, 4)

                    # org = (int(filtered_x[-1]), int(filtered_y[-1]))

                    # # 1 euro filter
                    # # org = (int(filters[i][0](time_frame, hand_landmarks.landmark[i].x * 640)), int(filters[i][1](time_frame, hand_landmarks.landmark[i].y * 480)))
                    # image = cv2.putText(image, str(i), org, font, fontScale, color, 1, cv2.LINE_AA, True)

                    org = (int(hand_landmarks.landmark[i].x * 1280), int(hand_landmarks.landmark[i].y * 960))
                    image = cv2.putText(image, str(i), org, font, fontScale, color, 1, cv2.LINE_AA, True)
                    start_point = (int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * 1280), int(
                        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * 960))
                    end_point = (int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * 1280), int(
                        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * 960))
                    mid_point = (int((start_point[0] + end_point[0]) / 2),
                                 int((start_point[1] + end_point[1]) / 2))
                    image = cv2.putText(image, str(round(math.dist(start_point, end_point), 2)),
                                        mid_point, font, fontScale, color, 1, cv2.LINE_AA, True)
                    image = cv2.line(image, start_point, end_point,
                                     color, thickness, cv2.LINE_AA)

                    if handedness.classification[0].label == 'Left':
                        point_index_left = (int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * 1280), int(
                            hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * 960))
                    else:
                        point_index_right = (int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * 1280), int(
                            hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * 960))
                    if point_index_right and point_index_left:
                        center_coordinates = (int((point_index_right[0] + point_index_left[0]) / 2), int(
                            (point_index_right[1] + point_index_left[1]) / 2))
                        # Draw a circle with blue line borders of thickness of 2 px
                        image = cv2.circle(image, center_coordinates, int(
                            math.dist(point_index_right, point_index_left) / 2), color, thickness)
                        image = cv2.line(image, point_index_right,
                                         point_index_left, color, thickness, cv2.LINE_AA)

                # mp_drawing.draw_landmarks(
                #     image,
                #     hand_landmarks,
                #     mp_hands.HAND_CONNECTIONS,
                #     mp_drawing_styles.get_default_hand_landmarks_style(),
                #     mp_drawing_styles.get_default_hand_connections_style())
                # Flip the image horizontally for a selfie-view display.

                # Plot the landmarks in matplotlib
                # plot_landmarks(hand_landmarks)
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
