from flask import Flask, render_template, request
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

import threading

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders

        remitente = "ekleain@gmail.com"
        password = "sbpl wmde xqat lhwy"
        destino = "ekleain@gmail.com"

        msg = MIMEMultipart()
        msg["Subject"] = "Nuevo reporte tecnico"
        msg["From"] = remitente
        msg["To"] = destino

        with open(archivo_pdf, "rb") as f:
            parte = MIMEBase("application", "octet-stream")
            parte.set_payload(f.read())

        encoders.encode_base64(parte)
        parte.add_header("Content-Disposition", f"attachment; filename={archivo_pdf}")

        msg.attach(parte)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(remitente, password)
        server.send_message(msg)
        server.quit()

    # correr en segundo plano
    threading.Thread(target=tarea).start()

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)