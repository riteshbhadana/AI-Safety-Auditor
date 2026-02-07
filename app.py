import os
import uuid
import streamlit as st

from vision.yolo_detector import YOLODetector
from utils.video_utils import read_video
from utils.image_utils import save_violation_image
from vision.gemini_vision import analyze_risk
from utils.pdf_utils import generate_pdf
from agent.safety_agent import run_safety_agent
from config.settings import YOLO_MODEL_PATH

# ---------------- STREAMLIT CONFIG ---------------- #
st.set_page_config(
    page_title="Agentic Safety Auditor",
    page_icon="🦺",
    layout="wide"
)

st.title("🦺 Agentic AI Safety Auditor")
st.write("Upload a construction/factory video and get an AI-generated safety audit report.")

# ---------------- CREATE REQUIRED FOLDERS ---------------- #
os.makedirs("data/uploads", exist_ok=True)
os.makedirs("data/violations", exist_ok=True)
os.makedirs("outputs/reports", exist_ok=True)

# ---------------- LOAD YOLO MODEL ---------------- #
@st.cache_resource
def load_yolo():
    return YOLODetector(YOLO_MODEL_PATH)

detector = load_yolo()

# ---------------- VIDEO UPLOAD ---------------- #
uploaded_video = st.file_uploader(
    "📤 Upload Site Video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video:
    video_id = uuid.uuid4().hex[:6]
    video_path = f"data/uploads/{video_id}_{uploaded_video.name}"

    with open(video_path, "wb") as f:
        f.write(uploaded_video.read())

    st.success("✅ Video uploaded successfully")

    if st.button("🚀 Start Safety Analysis"):
        st.info("Analyzing video… please wait ⏳")

        violation_found = False

        for frame in read_video(video_path):

            # 🔴 SINGLE SOURCE OF TRUTH
            violation = detector.detect_violation(frame)

            if violation:
                violation_found = True

                image_path = save_violation_image(
                    frame,
                    violation["person_bbox"]
                )

                st.image(
                    image_path,
                    caption="🚨 Detected Safety Violation",
                    width=400
                )

                # ---- Gemini Risk Reasoning ---- #
                with st.spinner("🧠 AI analyzing risk…"):
                    detection_summary = (
                        f"Violation: {violation['violation']}\n"
                        f"Severity: {violation['severity']}\n"
                        f"Location: {violation['person_bbox']}"
                    )

                    ai_analysis = analyze_risk(detection_summary)

                st.subheader("AI Risk Analysis")
                st.write(ai_analysis)

                # ---- Agent Decision ---- #
                decision = run_safety_agent(violation, ai_analysis)

                if decision["action"] == "GENERATE_REPORT":
                    report_path = f"outputs/reports/safety_report_{video_id}.pdf"

                    generate_pdf(
                        report_text=ai_analysis,
                        image_path=image_path,
                        output_path=report_path
                    )

                    st.success("📄 Safety audit report generated")

                    with open(report_path, "rb") as pdf:
                        st.download_button(
                            "⬇️ Download Safety Report",
                            pdf,
                            file_name=os.path.basename(report_path),
                            mime="application/pdf"
                        )

                break  # stop after first major violation

        if not violation_found:
            st.success("✅ No major safety violations detected.")
