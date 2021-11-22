from collect_data_iams import human_pose_data

data = human_pose_data()
# y.display_camera_with_mp()
data.collect_data_WHOLE()

#
# //uncomment the code below to collect data for Hand
# data.collect_data_HAND()

# //  uncomment the code below to collect data for Pose
# data.collect_data_POSE()

# //uncomment the code below to collect data for Face
# data.collect_data_FACE()

# data._whole_body()
# data._draw_only_hands()
# data._only_face()
# data._only_pose
