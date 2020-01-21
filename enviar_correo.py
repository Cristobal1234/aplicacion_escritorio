import smtplib
from decouple import config


def enviar_correo(correo_destino,imc,nombre):
    try:
        message  = "Buenos dias {}, tu imc es: ".format(nombre)+str(imc)
        subject  = "Notificacion de IMC"
        message  = "Subject:{}\n\n{}".format(subject,message)
        server   = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('cpadillar1995@gmail.com','@cristobal1995')
        server.sendmail('padillaruizcristobal@gmail.com',correo_destino,message)
        server.quit()
    except Exception as e:
        print(e)