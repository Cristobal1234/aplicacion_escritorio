
from tkinter import *
import eventos
import enviar_correo
import consumo_servicios
import time
###Eventos


window = Tk()
window.title("IMC")
label_nombre = Label(window, text="Ingrese nombre")
label_nombre.grid(column=5, row=5)
txt_nombre = Entry(window,width=10)
txt_nombre.grid(column=8, row=5)

label_email = Label(window, text="Ingrese email")
label_email.grid(column=5, row=10)
txt_email = Entry(window,width=10)
txt_email.grid(column=8, row=10)

label_peso = Label(window, text="Ingrese peso")
label_peso.grid(column=5, row=15)
txt_peso = Entry(window,width=10)
txt_peso.grid(column=8, row=15)


label_estatura = Label(window, text="Ingrese estatura")
label_estatura.grid(column=5, row=20)
txt_estatura = Entry(window,width=10)
txt_estatura.grid(column=8, row=20)

label_resultado = Label(window,text="Resultado")
label_resultado.grid(column=5, row=25)

def clicked():
    if txt_email.get()=="":
        label_resultado.configure(text="falta Email")
    elif txt_nombre.get()=="":
        label_resultado.configure(text="falta nombre")
    elif txt_estatura.get()=="":
        label_resultado.configure(text="falta estatura")
    elif txt_peso.get()=="":
        label_resultado.configure(text="falta peso")
    else:
        respuesta = consumo_servicios.pedir_imc(txt_nombre.get(),txt_estatura.get(),txt_peso.get())
        label_resultado.configure(text=str(respuesta))
        time.sleep(2)
        enviar_correo.enviar_correo(txt_email.get(),12,txt_nombre.get())
        

btn = Button(window, text="Enviar",command=clicked)
btn.grid(column=500, row=500)
window.geometry('900x800')
window.mainloop()
#padillaruizcristobal@gmail.com