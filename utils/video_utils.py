import cv2

def read_video(video_path, frame_skip=10):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_skip == 0:
            yield frame

        frame_count += 1

    cap.release()
