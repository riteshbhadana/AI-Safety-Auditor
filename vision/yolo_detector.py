# vision/yolo_detector.py

from ultralytics import YOLO

class YOLODetector:
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)

        # Labels (helmet requires PPE-trained model; logic still valid)
        self.PERSON_CLASS = "person"
        self.HELMET_CLASS = "helmet"

    def detect_violation(self, frame):
        """
        Detects safety violation:
        - Person detected
        - Helmet NOT detected on that person
        """

        results = self.model(frame, conf=0.4)
        boxes = results[0].boxes

        persons = []
        helmets = []

        for box in boxes:
            cls_id = int(box.cls[0])
            label = self.model.names[cls_id]
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if label == self.PERSON_CLASS:
                persons.append((x1, y1, x2, y2))

            elif label == self.HELMET_CLASS:
                helmets.append((x1, y1, x2, y2))

        # ---- REAL VIOLATION LOGIC ----
        for person_box in persons:
            if not self._helmet_on_person(person_box, helmets):
                return {
                    "violation": "Worker without safety helmet",
                    "severity": "HIGH",
                    "person_bbox": person_box
                }

        return None

    def _helmet_on_person(self, person_box, helmets):
        """
        Helmet must overlap top 25% of person bounding box
        """
        px1, py1, px2, py2 = person_box
        head_y = py1 + (py2 - py1) * 0.25

        for hx1, hy1, hx2, hy2 in helmets:
            if hx1 > px1 and hx2 < px2 and hy2 < head_y:
                return True

        return False
