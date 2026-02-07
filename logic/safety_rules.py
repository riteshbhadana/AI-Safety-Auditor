def check_safety_violation(detections, safe_distance=1000):
    persons = [d for d in detections if d["label"] == "person"]

    if persons:
        return {
            "violation": "Test Violation",
            "severity": "HIGH",
            "person_bbox": persons[0]["bbox"]
        }

    return None
