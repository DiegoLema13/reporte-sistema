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
        try:
            import os
            import base64
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

            message = Mail(
                from_email="TU_EMAIL_VERIFICADO@gmail.com",
                to_emails="TU_EMAIL@gmail.com",
                subject="Nuevo reporte tecnico",
                html_content="Adjunto reporte técnico"
            )

            # leer pdf
            with open(archivo_pdf, "rb") as f:
                data = base64.b64encode(f.read()).decode()

            attachment = Attachment(
                FileContent(data),
                FileName(archivo_pdf),
                FileType("application/pdf"),
                Disposition("attachment")
            )

            message.attachment = attachment

            sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
            response = sg.send(message)

            print("STATUS SENDGRID:", response.status_code)

        except Exception as e:
            print("ERROR SENDGRID:", str(e))

    import threading
    threading.Thread(target=tarea).start()

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)