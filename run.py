from collect_data_iams import human_pose_data

y = human_pose_data()
# y.display_camera_with_mp()
y.collect_data_WHOLE()
# from collect_data_iams_csv import human_pose_data
# y = human_pose_data()
# y.collect_data_WHOLE()
# import cv2
# cam = cv2.VideoCapture(0)
# # camera = cv2.VideoCapture(1)
# while True:
#     __, image = cam.read()
#     # _, image = camera.read()
#
#     cv2.imshow('Output eed', image)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break