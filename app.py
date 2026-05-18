from flask import Flask, render_template, request
import datetime
import threading
import os
import base64
import subprocess

from docxtpl import DocxTemplate
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail,
    Attachment,
    FileContent,
    FileName,
    FileType,
    Disposition,
)

app = Flask(__name__)


# ==============================================
# GENERAR DOCUMENTO WORD DESDE plantilla.docx
# ==============================================
def generar_documento(nombre, provincia, problema, fecha, archivo_docx):
    doc = DocxTemplate("plantilla.docx")

    contexto = {
        "nombre": nombre,
        "provincia": provincia,
        "problema": problema,
        "fecha": fecha,
    }

    doc.render(contexto)
    doc.save(archivo_docx)


# ==============================================
# CONVERTIR WORD A PDF (compatible con Render)
# ==============================================
def convertir_a_pdf(docx_path):
    subprocess.run(
        [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            docx_path,
            "--outdir",
            ".",
        ],
        check=True,
    )

# ==============================================
# ENVIAR CORREO CON PDF ADJUNTO
# ==============================================
def enviar_correo_async(archivo_pdf):
    def tarea():
        try:
            message = Mail(
                from_email="ekleain@gmail.com",  # cambia si deseas
                to_emails="ekleain@gmail.com",   # cambia si deseas
                subject="Nuevo reporte técnico",
                html_content="Se adjunta el reporte técnico en formato PDF.",
            )

            with open(archivo_pdf, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()

            attachment = Attachment(
                FileContent(encoded),
                FileName(os.path.basename(archivo_pdf)),
                FileType("application/pdf"),
                Disposition("attachment"),
            )

            message.attachment = attachment

            sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
            response = sg.send(message)

            print("Correo enviado. Status:", response.status_code)

        except Exception as e:
            print("Error al enviar correo:", str(e))

    threading.Thread(target=tarea).start()


# ==============================================
# RUTA PRINCIPAL
# ==============================================
@app.route("/")
def home():
    return render_template("formulario.html")


# ==============================================
# PROCESAR FORMULARIO
# ==============================================
@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form["nombre"]
    provincia = request.form["provincia"]
    problema = request.form["problema"]

    # Formato de fecha sugerido: 18-05-2026
    fecha = datetime.datetime.now().strftime("%d-%m-%Y")

    archivo_docx = "reporte_tecnico.docx"
    archivo_pdf = "reporte_tecnico.pdf"

    # 1. Generar Word desde la plantilla
    generar_documento(
        nombre=nombre,
        provincia=provincia,
        problema=problema,
        fecha=fecha,
        archivo_docx=archivo_docx,
    )

    # 2. Convertir a PDF
    convertir_a_pdf(archivo_docx)

    # 3. Enviar PDF por correo
    enviar_correo_async(archivo_pdf)

    return "Reporte enviado correctamente."


# ==============================================
# EJECUCIÓN LOCAL
# ==============================================
if __name__ == "__main__":
    app.run(debug=True)