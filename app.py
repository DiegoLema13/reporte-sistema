from flask import Flask, render_template, request
import datetime
import threading
import os
import base64

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
def generar_documento(
    nombre,
    cedula,
    provincia,
    delegada,
    modelo,
    series,
    problema,
    fecha,
    archivo_docx
):
    
    doc = DocxTemplate("plantilla.docx")

    filas = []

    for i, serie in enumerate(series):

        filas.append({
            "provincia": provincia if i == 0 else "",
            "detalle": "Impresora Financiera" if i == 0 else "",
            "modelo": modelo if i == 0 else "",
            "serie": serie
        })

    contexto = {
        "nombre": nombre,
        "cedula": cedula,
        "provincia": provincia,
        "delegada": delegada,
        "problema": problema,
        "fecha": fecha,
        "filas": filas
    }

    doc.render(contexto)
    doc.save(archivo_docx)

# ==============================================
# ENVIAR CORREO CON DOCX ADJUNTO
# ==============================================
def enviar_correo_async(archivo):

    def tarea():
        try:
            message = Mail(
                from_email="ekleain@gmail.com",
                to_emails="ekleain@gmail.com",
                subject="Nuevo reporte técnico",
                html_content="Adjunto reporte técnico generado automáticamente.",
            )

            # Leer el archivo DOCX
            with open(archivo, "rb") as f:
                data = base64.b64encode(f.read()).decode()

            # Adjuntar el archivo Word
            attachment = Attachment(
                FileContent(data),
                FileName(os.path.basename(archivo)),
                FileType(
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                ),
                Disposition("attachment"),
            )

            message.attachment = attachment

            # Enviar usando SendGrid
            sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
            response = sg.send(message)

            print("STATUS SENDGRID:", response.status_code)

        except Exception as e:
            print("ERROR SENDGRID:", str(e))

    threading.Thread(target=tarea).start()

# ==============================================
# FORMULARIO
# ==============================================
@app.route("/")
def home():
    return render_template("formulario.html")

# ==============================================
# PROCESAR FORMULARIO
# ==============================================
@app.route("/enviar", methods=["POST"])
def enviar():

    # Obtener datos del formulario
    nombre = request.form["nombre"]

    cedula = request.form["cedula"]

    provincia = request.form["provincia"]

    delegada = request.form["delegada"]

    problema = request.form["problema"]

    modelo = request.form["modelo"]

    # Obtener múltiples series
    series = request.form.getlist("series[]")

    # Mostrar series en consola
    print("SERIES RECIBIDAS:")

    print(series)

    # Formato de fecha
    fecha = datetime.datetime.now().strftime("%d-%m-%Y")

    # Archivo de salidaa
    archivo_docx = "reporte_tecnico.docx"

    

    # Generar documento Word basado en la plantilla
    generar_documento(
        nombre=nombre,
        cedula=cedula,
        provincia=provincia,
        delegada=delegada,
        problema=problema,
        modelo=modelo,
        series=series,
        fecha=fecha,
        archivo_docx=archivo_docx,
    )

    # Enviar el documento por correo
    enviar_correo_async(archivo_docx)

    return render_template("exito.html")


# ==============================================
# EJECUCIÓN LOCAL
# ==============================================
if __name__ == "__main__":
    app.run(debug=True)