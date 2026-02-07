title: Agentic AI Safety Auditor
emoji: 🦺
colorFrom: indigo
colorTo: purple
sdk: streamlit
sdk_version: 1.44.1
app_file: app.py
pinned: false

# 🦺 Agentic AI Safety Auditor

An end-to-end **Agentic AI system** that analyzes construction or factory site videos to automatically detect safety violations, assess risk severity using AI reasoning, and generate professional safety audit reports.

🚀 **Built for real-world workplace safety monitoring and AI/ML interviews**

---

## 🔍 What This Project Does

This system takes a **video feed** from a construction or industrial site and:

1. **Detects safety violations** using a YOLO-based vision model  
   - Example: Worker detected **without a safety helmet**
2. **Analyzes risk severity** using an AI language model (Gemini, optional)
3. **Generates actionable recommendations** like a real safety auditor
4. **Automatically produces a PDF safety audit report**
5. **Runs end-to-end via a simple web interface**

---

## 🧠 Why This Project Is Impressive

- ✅ Uses **Agentic AI** (Detect → Reason → Act)
- ✅ Combines **Computer Vision + LLM reasoning**
- ✅ Solves a **real industrial problem** (workplace safety)
- ✅ End-to-end product (not just a model)
- ✅ Deployable on Hugging Face / Streamlit
- ✅ Interview & portfolio ready

---

## 🏗️ System Architecture

Video Upload
↓
Frame Sampling
↓
YOLO Vision Model
↓
Safety Violation Detection
↓
AI Risk Reasoning (Gemini / Offline)
↓
Safety Agent Decision
↓
PDF Audit Report Generation


---

## 🧪 Example Safety Violation Detected

- 🚨 **Worker without safety helmet**
- ⚠️ Severity: **HIGH**
- 📍 Localized using bounding box
- 📄 Professional audit report generated automatically

---

## 🌐 Live Demo

👉 **Hugging Face Space:**  
(Add your HF Space link here)

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/agentic-safety-auditor.git
cd agentic-safety-auditor
2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ (Optional) Set Gemini API Key
set GEMINI_API_KEY=your_api_key_here   # Windows (temporary)
If no API key is provided, the app runs in offline reasoning mode.

5️⃣ Run the app
streamlit run app.py
Open browser:

http://localhost:8501
☁️ Deployment
✔ Hugging Face Spaces (Recommended)
SDK: Streamlit

Hardware: CPU

Secrets:

GEMINI_API_KEY (optional)

✔ Streamlit Community Cloud
Direct GitHub deployment

Add secrets in Streamlit dashboard

❌ Docker is not required for deployment.

🔐 Security & Reliability
No API keys stored in code

Secrets injected via environment variables

Graceful fallback if LLM quota is unavailable

CPU-only inference for broad compatibility

🧠 Interview Explanation (One-Liner)
“I built an Agentic AI Safety Auditor that combines real-time computer vision with LLM-based reasoning to automatically detect workplace safety violations and generate audit-ready reports.”

📌 Tech Stack
Frontend: Streamlit

Vision: YOLO (Ultralytics)

AI Reasoning: Google Gemini (optional)

PDF Generation: ReportLab

Deployment: Hugging Face Spaces / Streamlit Cloud

📈 Future Improvements
Additional PPE detection (vest, gloves)

Machinery proximity risk analysis

Violation confidence scoring

Multi-violation reporting

Real-time camera stream support

👤 Author
Your Name
AI / ML Engineer