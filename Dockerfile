# ---- Base Image ----
FROM python:3.10-slim

# ---- Environment Settings ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- System Dependencies ----
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# ---- Working Directory ----
WORKDIR /app

# ---- Copy Requirements ----
COPY requirements.txt .

# ---- Install Python Dependencies ----
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ---- Copy Project Code ----
COPY . .

# ---- Create Required Runtime Directories ----
RUN mkdir -p data/uploads data/violations outputs/reports

# ---- Expose Streamlit Port ----
EXPOSE 8501

# ---- Run Streamlit App ----
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
