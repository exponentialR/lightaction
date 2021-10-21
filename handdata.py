import cv2
import numpy as np
import os
from matplotlib import pyplot
import time
import mediapipe as mp

mp_hands = mp.solutions.hands  # Holistic model
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic  # Drawing utilities


class sequential_data:
    def __init__(self):
        # self.states, self.pathdir, self.len_seq, self.len_fold = make_sequence_folder()
        self.solutions = mp.solutions.holistic
        self.draw = mp.solutions.drawing_utils
        self.holistic = self.solutions.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.hand_connect = self.solutions.HAND_CONNECTIONS
        self.pose_connect = self.solutions.POSE_CONNECTIONS
        self.face_connect = self.solutions.FACEMESH_TESSELATION
        self.actions = []

    def hand_Detection(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
        image.flags.writeable = False  # Image is no longer writeable
        coords = self.holistic.process(image)  # Make prediction
        image.flags.writeable = True  # Image is now writeable
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR
        return image, coords

    def draw_landmarks(self, image, coords):
        self.draw.draw_landmarks(image, coords.left_hand_landmarks, self.hand_connect)  # Draw left hand connections
        self.draw.draw_landmarks(image, coords.right_hand_landmarks, self.hand_connect)  # Draw right hand
        self.draw.draw_landmarks(image, coords.face_landmarks, self.face_connect)
        self.draw.draw_landmarks(image, coords.pose_landmarks, self.pose_connect)


    def extract_keypoints(self, coords):
        """Function to extract coordinates of keypoints on both hands"""
        right_hand = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                               coords.right_hand_landmarks.landmark]).flatten() if coords.right_hand_landmarks else np.zeros(
            21 * 3)
        left_hand = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                              coords.left_hand_landmarks.landmark]).flatten() if coords.left_hand_landmarks else np.zeros(
            21 * 3)
        full_body = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in coords.pose_landmarks]).flatten() if coords.pose_landmarks else np.zeros(132)
        facial = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in coords.face_landmarks]).flatten() if coords.face_landmarks else np.zeros(1)
        return np.concatenate([right_hand, left_hand, full_body, facial])

        # lh, rh = [], []
        # for ids, hand_landmarks in enumerate(results.multi_hand_landmarks):
        #     if ids == 0:
        #         lh = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
        #                        hand_landmarks.landmark]).flatten() if True else np.zeros(21 * 3)
        #     if ids == 1:
        #         rh = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
        #                        hand_landmarks.landmark]).flatten() if True else np.zeros(21 * 3)
        # # x = np.concatenate([lh, rh])
        # # return x.tolist()
        #     return np.concatenate([lh, rh])

    def display_camera_with_mp(self):
        camera = cv2.VideoCapture(0)
        while True:
            ret, image = camera.read()
            image = cv2.flip(image, 1)
            frame, coords = self.hand_Detection(image)
            self.draw_landmarks(frame, coords)
            cv2.imshow('Output_Feed', frame)

            if cv2.waitKey(10) == ord('q'):
                # break
                camera.release()
                cv2.destroyAllWindows()


    def collect_data(self):
        while self.display_camera_with_mp():



#
#
# actions, DATA_PATH, no_sequences, sequence_length = make_sequence_folder()
# cap = cv2.VideoCapture(0)
# # Set mediapipe model
# with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5) as hands:
#     for action in actions:
#         # Loop through sequences aka videos
#         for sequence in range(no_sequences):
#             # Loop through video length aka sequence length
#             for frame_num in range(sequence_length):
#
#                 # Read feed
#                 ret, frame = cap.read()
#
#                 # Make detections
#                 image, results = mediapipe_detection(frame, hands)
#                 #                 print(results)
#
#                 # Draw landmarks
#                 draw_landmarks(image, results)
#
#                 # NEW Apply wait logic
#                 if frame_num == 0:
#                     cv2.putText(image, 'STARTING COLLECTION', (120, 200),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
#                     cv2.putText(image, 'Collecting frames for {}  {}'.format(action, sequence), (15, 12),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
#                     # Show to screen
#                     cv2.imshow('OpenCV Feed', image)
#                     cv2.waitKey(2000)
#                 else:
#                     cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15, 12),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
#                     # Show to screen
#                     cv2.imshow('OpenCV Feed', image)
#
#                 # NEW Export keypoints
#                 keypoints = extract_keypoints(results)
#                 npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
#                 np.save(npy_path, keypoints)
#
#                 # Break gracefully
#                 if cv2.waitKey(10) & 0xFF == ord('q'):
#                     break
#
#     cap.release()
#     cv2.destroyAllWindows()

