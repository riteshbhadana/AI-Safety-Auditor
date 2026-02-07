# utils/image_utils.py

import cv2
import os
import uuid

def save_violation_image(frame, bbox, save_dir="data/violations"):
    os.makedirs(save_dir, exist_ok=True)

    x1, y1, x2, y2 = bbox
    cropped = frame[y1:y2, x1:x2]

    filename = f"violation_{uuid.uuid4().hex[:6]}.jpg"
    path = os.path.join(save_dir, filename)

    cv2.imwrite(path, cropped)
    return path
