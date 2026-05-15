from flask import Flask, render_template, request
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

import threading

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import base64

import os



app = Flask(__name__)


# =========================
# PDF CON REPORTLAB
# =========================
def generar_pdf(nombre, provincia, problema, fecha, archivo_pdf):
    c = canvas.Canvas(archivo_pdf, pagesize=letter)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(180, 750, "REPORTE TECNICO")

    c.setFont("Helvetica", 11)
    c.drawString(100, 700, f"Nombre: {nombre}")
    c.drawString(100, 680, f"Provincia: {provincia}")
    c.drawString(100, 660, f"Problema: {problema}")
    c.drawString(100, 640, f"Fecha: {fecha}")

    c.save()


# =========================
# FORMULARIO
# =========================
@app.route("/")
def home():
    return render_template("formulario.html")


# =========================
# ENVIAR FORMULARIO
# =========================
@app.route("/enviar", methods=["POST"])
def enviar():

    nombre = request.form["nombre"]
    provincia = request.form["provincia"]
    problema = request.form["problema"]
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    pdf_file = "reporte.pdf"

    generar_pdf(nombre, provincia, problema, fecha, pdf_file)

    # 🚀 ahora sí activamos correo sin bloquear
    enviar_correo_async(pdf_file)

    return "Reporte recibido ✔ PDF generado y enviado por correo"

# =========================
# CORREO
# =========================
def enviar_correo_async(archivo_pdf):

    def tarea():
        import threading

        message = Mail(
            from_email="ekleain@gmail.com",
            to_emails="ekleain@gmail.com",
            subject="Nuevo reporte tecnico",
            html_content="<strong>Adjunto reporte técnico</strong>"
        )

        with open(archivo_pdf, "rb") as f:
            import base64
            encoded_file = base64.b64encode(f.read()).decode()

        message.attachment = {
            "content": encoded_file,
            "type": "application/pdf",
            "filename": archivo_pdf,
            "disposition": "attachment"
        }
        sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
        sg.send(message)

    threading.Thread(target=tarea).start()

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)