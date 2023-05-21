import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text()) # creamos un objeto template 

# creamos el correo
email = EmailMessage()
email['from_addr'] = 'Manuel Simarro' # Dirección
email['To'] = 'manu.g1501@gmail.com' # correo al que se lo enviamos
email['subject'] = 'Enviando correo desde python' # asunto
email.set_content(html.substitute({'name':'TinTin'}), 'html') # dentro del contenido de correo, usamos el objeto Template

# conectando a mi cuenta de gmail
with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:  
    # empezando protocolo de saludo
    smtp.ehlo()
    smtp.starttls

    # haciendo login
    smtp.login('manuelsimarro.1501@gmail.com', 'tddqbhdivurhxcbp')

    # enviando el objeto correo
    smtp.send_message(email)

    # comprobación de que el mensaje se ha enviado
    print('all good')