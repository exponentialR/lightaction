import cv2
import numpy as np
import mediapipe as mp
import os
from pathlib import Path
import json

mp_hands = mp.solutions.hands  # Holistic model
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic  # Drawing utilities


class sequential_data:
    def __init__(self):
        # self.states, self.pathdir, self.len_seq, self.len_fold = make_sequence_folder()
        self.solutions = mp.solutions.holistic
        self.draw = mp.solutions.drawing_utils
        self.holistic = self.solutions.Holistic(min_detection_confidence=0.3, min_tracking_confidence=0.3)
        self.hand_connect = self.solutions.HAND_CONNECTIONS
        self.pose_connect = self.solutions.POSE_CONNECTIONS
        self.face_connect = self.solutions.FACEMESH_TESSELATION
        # self.hands = mp_hands

    def Detection_pipeline(self, image, holistic):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
        image.flags.writeable = False  # Image is no longer writeable
        coords = holistic.process(image)  # Make prediction
        image.flags.writeable = True  # Image is now writeable
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR
        return image, coords

    def draw_landmarks(self, image, coords):
        self.draw.draw_landmarks(image, coords.left_hand_landmarks, self.hand_connect)  # Draw left hand connections
        self.draw.draw_landmarks(image, coords.right_hand_landmarks, self.hand_connect)  # Draw right hand
        self.draw.draw_landmarks(image, coords.face_landmarks, self.face_connect)
        self.draw.draw_landmarks(image, coords.pose_landmarks, self.pose_connect)

    def draw_only_hands(self):
        camera = cv2.VideoCapture(0)
        while True:
            with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
                _, image = camera.read()
                image = cv2.flip(image, 1)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                coords = hands.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if coords.multi_hand_landmarks:

                    for idx, hand_landmark in enumerate(coords.multi_hand_landmarks):

                        self.draw.draw_landmarks(image, hand_landmark, mp_hands.HAND_CONNECTIONS,
                                                 self.draw.DrawingSpec(color=(255, 0, 200), thickness=1, circle_radius=3),
                                                 self.draw.DrawingSpec(color=(150, 120, 255), thickness=1, circle_radius=2), )
                    for _, classification in enumerate(coords.multi_handedness):
                        if classification.classification[0].index == idx and classification.classification[0].index ==1:
                            hand_label = classification.classification[0].label
                            coord = tuple(
                                np.multiply(np.array((hand_landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x, hand_landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)), [640, 480]).astype(int))
                            text = '{} {}'.format(hand_label, coord)
                            cv2.putText(image, text, coord, cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 100, 200), 2, cv2.LINE_AA)

                        elif classification.classification[0].index == idx:
                            hand_label = classification.classification[0].label
                            coord = tuple(
                                np.multiply(np.array((hand_landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x, hand_landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)), [640, 480]).astype(int))
                            text = '{} {}'.format(hand_label, coord)
                            cv2.putText(image, text, coord, cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 100, 200), 2, cv2.LINE_AA)
                        else:
                            # classification.classification[0].index == 1:
                            hand_label = classification.classification[0].label
                            coord = tuple(
                                np.multiply(np.array((hand_landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,
                                                      hand_landmark.landmark[
                                                          mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)),
                                            [640, 480]).astype(int))
                            text = '{} {}'.format(hand_label, coord)
                            cv2.putText(image, text, coord, cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 100, 200), 2,
                                        cv2.LINE_AA)
                cv2.imshow('Output Hand-Tracking', image)
                if cv2.waitKey(10) != ord('q'):

                    continue
                camera.release()
                cv2.destroyAllWindows()

    def Draw_only_face(self):

        camera = cv2.VideoCapture(0)

        with self.holistic as holistic:
            while True:
                ret, image = camera.read()
                image = cv2.flip(image, 1)
                frame, coords = self.Detection_pipeline(image, holistic)
                self.draw.draw_landmarks(image, coords.face_landmarks, self.face_connect)
                cv2.imshow('Output_Feed Facial', frame)

                if cv2.waitKey(10) != ord('q'):
                    continue
                camera.release()
                cv2.destroyAllWindows()


    def Draw_only_pose(self):
        camera = cv2.VideoCapture(0)

        with self.holistic as holistic:
            while True:
                ret, image = camera.read()
                image = cv2.flip(image, 1)
                frame, coords = self.Detection_pipeline(image, holistic)
                self.draw.draw_landmarks(image, coords.pose_landmarks, self.pose_connect)
                cv2.imshow('Output_Feed Facial', frame)

                if cv2.waitKey(10) != ord('q'):
                    continue
                camera.release()
                cv2.destroyAllWindows()


    def extract_full_body(self, coords):
        """Function to extract coordinates of keypoints on both hands"""
        right_hand = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                               coords.right_hand_landmarks.landmark]).flatten() if coords.right_hand_landmarks else np.zeros(
            21 * 3)
        left_hand = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                              coords.left_hand_landmarks.landmark]).flatten() if coords.left_hand_landmarks else np.zeros(
            21 * 3)
        pose = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                         coords.pose_landmarks]).flatten() if coords.pose_landmarks else np.zeros(132)
        facial = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                           coords.face_landmarks]).flatten() if coords.face_landmarks else np.zeros(1)
        return np.concatenate([right_hand, left_hand, pose, facial])

    def extract_only_hands(self, coords):
        """this function extracts only coordinates of the hands"""
        right_hand = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                               coords.right_hand_landmarks.landmark]).flatten() if coords.right_hand_landmarks else np.zeros(
            21 * 3)
        left_hand = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                              coords.left_hand_landmarks.landmark]).flatten() if coords.left_hand_landmarks else np.zeros(
            21 * 3)
        return np.concatenate([left_hand, right_hand])

    def extract_only_facial(self, coords):
        return np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                         coords.face_landmarks]).flatten() if coords.face_landmarks else np.zeros(1)

    def extract_only_pose(self, coords):
        return np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
                         coords.pose_landmarks]).flatten() if coords.pose_landmarks else np.zeros(132)

        # lh, rh = [], []
        # for ids, hand_landmarks in enumerate(results.multi_hand_landmarks):
        #     if ids == 0:
        #         lh = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
        #                        hand_landmarks.landmark]).flatten() if True else np.zeros(21 * 3)
        #     if ids == 1:
        #         rh = np.array([[landmarked.x, landmarked.y, landmarked.z] for landmarked in
        #                        hand_landmarks.landmark]).flatten() if True else np.zeros(21 * 3)
        # x = np.concatenate([lh, rh])
        # return x.tolist()
        #     return np.concatenate([lh, rh])

    def Draw_whole_body(self):
        camera = cv2.VideoCapture(0)
        with self.holistic as holistic:
            while True:
                ret, image = camera.read()
                image = cv2.flip(image, 1)
                frame, coords = self.Detection_pipeline(image, holistic)
                self.draw_landmarks(frame, coords)
                cv2.imshow('Output_Feed Whole Body', frame)

                if cv2.waitKey(10) != ord('q'):
                    continue
                camera.release()
                cv2.destroyAllWindows()

#
    def collect_data(self):
        camera = cv2.VideoCapture(0)
        """
        Get current working directory
        Get the list of actions
        get the number of subfolders
        iterate through them"""
        cur_scr_dir = os.path.dirname(__file__) #This is the absolute directory the script is in
        relative_data_path = "data/iamsMediapipe.iams"
        abs_iams_path = Path(os.path.join(cur_scr_dir, relative_data_path))

        f = open(abs_iams_path)
        f_content = json.load(f)
        with self.holistic as holistic:
            for action in f_content['actions']:
                for folder in range(0, len(f_content['subfolder_length'])):
                    for img_ in range(len(f_content['video_length'])):
                        _, image = camera.read()
                        image, coords = self.Detection_pipeline(image, holistic)
                        if img_ == 0:
                            cv2.putText(image, 'Starting Data Collection into {}'.format(f_content['Data_Directory']),
                                        (100, 100), cv2.FarnebackOpticalFlow, 1, (120, 100, 150), 3, cv2.LINE_AA)
                            cv2.putText(image, 'Now Collecting Data for {}; {}'.format(action, folder),
                                        (15, 12), cv2.FarnebackOpticalFlow, 1, (120, 100, 150), 3, cv2.LINE_AA)
                            cv2.imshow('Data Collection Feed', image)
                            cv2.waitKey(2000)

                        else:
                            cv2.putText(image, 'Now Collecting Data for {}; {}'.format(action, folder),
                                        (15, 12), cv2.FarnebackOpticalFlow, 1, (120, 100, 150), 3, cv2.LINE_AA)
                            cv2.imshow('Data Collection Feed', image)

                        keypoints = self.extract_full_body(coords)
                        keypoint_path = os.path.join(f_content['Data_Subfolder'], action, str(folder), str(img_))
                        np.save(keypoint_path, keypoints)
                        if cv2.waitKey(10) != ord('q'):
                            continue
                        camera.release()
                        cv2.destroyAllWindows()