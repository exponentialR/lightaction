import cv2
cam = cv2.VideoCapture(0
                       )
while True:
    _, image = cam.read()
    image_height, image_width, _= image.shape # cv2.imshow('Output Feed ', image)
    print(image_height)