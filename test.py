# import cv2
# import mediapipe as mp
# import numpy as np
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
# camera = cv2.VideoCapture(0)
# with mp_hands.Hands(min_tracking_confidence=0.5, min_detection_confidence=0.5) as hands:
#     while True:
#         _, image = camera.read()
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image.flags.writeable = False
#         results = hands.process(image)
#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#
#         if results.multi_hand_landmarks:
#             # for hand_landmarks in (results.multi_hand_landmarks):
#             #     mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             #     cv2.imshow('Output Feed, Image', image)
#             #     # left_hand = []
#             for idx, hand_landmark in enumerate(results.multi_hand_landmarks):
#                 for _, classification in enumerate(results.multi_handedness):
#                     # if classification.classification[0].index == 1:# and classification.classification[0].index == 1:
#                     right_hand = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in hand_landmark.landmark]).flatten() if classification.classification[0].index == 1 else np.zeros(21*3)
#
#                         # hand_label = classification.classification[0].label #====> right hand
#                         # print(hand_label)
#
#                     # if classification.classification[0].index == idx:
#                     left_hand = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in hand_landmark.landmark]).flatten() if classification.classification[0].index == idx else np.zeros(21*3)
#                     keypoints = np.concatenate([right_hand, left_hand])
#                     print(keypoints)
#                     print(len(keypoints))
#                     # print(left_hand)
#                     # print(right_hand)
#                     # print(len(right_hand))
#                     # print(len(left_qqhand))
#                     #
#                     #     hand_label = classification.classification[0].label
#                     #     print(hand_label) # ===> left
#                     #     coord = tuple(
#                     #         np.multiply(np.array((hand_landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,
#                     #                               hand_landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)),
#                     #                     [640, 480]).astype(int))
#                     #     text = '{} {}'.format(hand_label, coord)
#                     #     cv2.putText(image, text, coord, cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 100, 200), 2, cv2.LINE_AA)
#                     # elif classification.classification[0].index == 1:
#                     # hand_label = classification.classification[0].label
#                     # cv2.imshow('o', image)
#                     #     coord = tuple(
#                     #         np.multiply(np.array((hand_landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,
#                     #                               hand_landmark.landmark[
#                     #                                   mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)),
#                     #                     [640, 480]).astype(int))
#                     #     text = '{} {}'.format(hand_label, coord)
#                     #     cv2.putText(image, text, coord, cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 100, 200), 2,
#                     #                 cv2.LINE_AA)
#
#
#                 # handlist = np.array([[landmarked.x, landmarked.y, landmarked.z] for ids, landmarked in enumerate( hand_landmarks.landmark)]).flatten() if hand_landmarks.landmark else np.zeros(42 * 3)
#
#                 # right_hand = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
#                 #                                    hand_landmarks.landmark]).flatten() if True else np.zeros(21 * 3)
#             # print(handlist)
#             # print(len(handlist))
#             # print(right_hand)
#             # keypoint = np.concatenate([left_hand, right_hand])
#             # print(len(keypoint))
#
#             # print('Right hand: ' + right_hand)
#             # print('Right hand: ' + str(len(right_hand)))
#             # print(keypoint)
#             if cv2.waitKey(10) != ord('q'):
#                 continue
#             camera.release()
#             cv2.destroyAllWindows()
import os.path

import cv2

actions = ['lick', 'nod', 'open_mouth', 'wave']


def loop_through(actions, num1, num2):
    for action in actions:
        for i in range(num1, num1+num2):
            for m in range(0, num2):
                return action, i, m

from pathlib import Path
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Also try reading video from self.
import numpy as np


k = 0
action, i, m = loop_through(actions, 3, 3)
for action in actions:
    for sequence in range(30, 60):
        for frame_num in range(30):
            if frame_num == 0:
                print('We are starting collection')
            else:
                print(' We wil wait a while')

