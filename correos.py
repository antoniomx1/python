import pandas as pd
import yagmail

def send_email_with_attachment(receiver_email, subject, body, attachment_path):
    """
    Envía un correo electrónico con un archivo adjunto.

    :param receiver_email: Dirección de correo electrónico del destinatario.
    :param subject: Asunto del correo electrónico.
    :param body: Cuerpo del correo electrónico.
    :param attachment_path: Ruta del archivo a adjuntar.
    """
    # credenciales de correo
    yag = yagmail.SMTP(user='direccion_academica@utel.mx', password='3ef8uttoz2QE', host='smtp.utel.mx', port=465)
    
    # Enviar el correo
    yag.send(
        to=receiver_email,
        subject=subject,
        contents=body,
        attachments=attachment_path,
    )

def main():
    # Leer el archivo csv
    df = pd.read_csv('archivo.csv',encoding='latin1')
    
    for index, row in df.iterrows():
        docente = row['Docente']
        emaildocente = row['email_profesor']
        archivo_ruta = row['Ruta']
        matricula=row['Mat_Docente']
        subject = f"Publicacion formacion de equipos"
         # Cuerpo del mensaje en formato HTML
        body_html = f"""
          <html>
Texto html
</html>
        """
        
        send_email_with_attachment(emaildocente, subject, body_html, archivo_ruta)
        print(f"Correo enviado a {matricula} ({emaildocente})")

if __name__ == "__main__":
    main()
