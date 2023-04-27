import cv2
import numpy as np


def add_video_to_image(image_path, video_path, output_path, x, y, w, h):
    # Load the image and the video
    img = cv2.imread(image_path)
    video = cv2.VideoCapture(video_path)

    # Get the video codec and frame size
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a video writer object
    out = cv2.VideoWriter(output_path, fourcc, 30.0,
                          (img.shape[1], img.shape[0]))

    # Loop through the frames in the video
    while True:
        # Read a frame from the video
        ret, frame = video.read()

        # If the frame is not valid, break out of the loop
        if not ret:
            break

        # Resize the video frame to match the face size
        frame = cv2.resize(frame, (w, h))

        # Paste the video frame onto the face region in the image
        img[y:y+h, x:x+w] = frame

        # Write the updated image to the output video
        out.write(img)

    # Release the video and image objects
    video.release()
    out.release()


add_video_to_image("Insta-3.jpg", "output/result.mp4",
                   "output_vid.mp4", 30, 0, 730, 730)
