# vision/gemini_vision.py
# Gemini API – FREE TIER SAFE MODEL

import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_risk(detection_summary: str) -> str:
    prompt = f"""
    You are a professional workplace safety auditor.

    Based on the following detection summary from a construction site,
    analyze the safety risk, classify severity as LOW, MEDIUM, or HIGH,
    and give a short actionable recommendation.

    Detection Summary:
    {detection_summary}
    """

    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=prompt
    )

    return response.text
