# utils/pdf_utils.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_pdf(report_text, image_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    c = canvas.Canvas(output_path, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "AI Safety Audit Report")

    c.setFont("Helvetica", 12)
    text = c.beginText(50, 750)

    for line in report_text.split("\n"):
        text.textLine(line)

    c.drawText(text)

    c.drawImage(image_path, 50, 200, width=300, preserveAspectRatio=True)
    c.save()
