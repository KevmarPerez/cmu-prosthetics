import os
import cv2
import numpy as np
import mediapipe as mp

# Store background images in a  list
image_path = 'images'
images = os.listdir(image_path)

image_index = 0
bg_image = cv2.imread(image_path+'/'+images[image_index])

# initialize mediapipe
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    # flip the frame to horizontal direction
    frame = cv2.flip(frame,1)
    height, width, channel = frame.shape

    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get the result
    results = selfie_segmentation.process(RGB)

    # extract segmented mask
    mask = results.segmentation_mask

    # it returns true or false where the condition applies in the mask
    condition = np.stack((mask,) * 3, axis=-1) > 0.5

    # resizing the background image to the same size of the original frame
    bg_image = cv2.resize(bg_image, (width, height))

    #combine frame and background image using the condition
    output_image = np.where(condition, frame, bg_image)

    # show outputs
    cv2.imshow("mask", output_image)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

    # if 'd' key is pressed then change the ackground image

    elif key == ord('d'):
        if image_index != len(images)-1:
            image_index += 1
        else:
            image_index = 0
        bg_image = cv2.imread(image_path+'/'+images[image_index])

