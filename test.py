# import os.path
#
# import numpy as np
# list1 = np.array([[121, 112, 220]]).flatten()
# list2 = np.array([[223, 224, 223]]).flatten()
# list3 = np.array([17, 112]).flatten()
# x = np.concatenate([list1, list2])
# y = np.concatenate([x, list3])#list3])
# print(y)
# print(os.path.dirname(__file__))
#
#
# # y = np.concatenate([x, list3])
# # print(y)


hand_landmark = {0: 'WRIST', 1: 'THUMB_CMC',
                                 2: 'THUMB_MCP',
                                 3: 'THUMB_IP',
                                 4: 'THUMB_TIP',
                                 5: 'INDEX_FINGER_MCP',
                                 6: 'INDEX_FINGER_PIP',
                                 7: 'INDEX_FINGER_DIP',
                                 8: 'INDEX_FINGER_TIP',
                                 9: 'MIDDLE_FINGER_MCP',
                                 10: 'MIDDLE_FINGER_PIP',
                                 11: 'MIDDLE_FINGER_DIP',
                                 12: 'MIDDLE_FINGER_TIP',
                                 13: 'RING_FINGER_MCP',
                                 14: 'RING_FINGER_PIP',
                                 15: 'RING_FINGER_DIP',
                                 16: 'RING_FINGER_TIP',
                                 17: 'PINKY_MCP',
                                 18: 'PINKY_PIP',
                                 19: 'PINKY_DIP',
                                 20: 'PINKY_TIP'}

empty_list = []
for k, v in hand_landmark.items():
    for i in range(3):
        empty_list.append(v)

hand_landmark_x_y_z = [['{}_x'.format(x), '{}_y'.format(y), '{}_z'.format(z)] for x, y, z in
zip(empty_list[0::3], empty_list[1::3], empty_list[2::3])]

hand_landmark_x_y_z = [item for sublist in hand_landmark_x_y_z for item in sublist]
print(hand_landmark_x_y_z)
iams_dict = {'csv_header': hand_landmark_x_y_z}
for i in range(len(iams_dict['csv_header'])):
    print(iams_dict['csv_header'][i])

