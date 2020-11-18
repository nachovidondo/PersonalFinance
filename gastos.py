from tkinter import*
from datetime import datetime
from consulta import *
import time
import locale
import sqlite3
from tkinter import messagebox

ventana = Tk()
ventana.geometry("1200x600")
ventana.iconbitmap("icon.ico")
ventana.title("Sistema Contable del Hogar")
ventana.resizable(width=False, height=False)

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dateTimeNow = datetime.now()
currentDate = dateTimeNow.strftime("%A %d, %B %Y")
currentTime = dateTimeNow.strftime("%I:%M %p")

dbConnection = None

def persist(savedTime,textAlquiler,textAuto,textSupermercado,textServicios,textTarjetaCredito,textTransporte,textObraSocial,textRecreativos,textIngresoMama,textIngresoPapa):
    dbConnection = Consult()
    print("Conexion : ", dbConnection.con)
    dbConnection.insertData(savedTime,textAlquiler,textAuto,textSupermercado,textServicios,textTarjetaCredito,textTransporte,textObraSocial,textRecreativos,textIngresoMama,textIngresoPapa)
    


def enviarDatos():
    textAlquiler = text_Alquiler.get()
    textAuto = text_Auto.get()
    textSupermercado = text_Supermercado.get()
    textServicios = text_Servicios.get()
    textTarjetaCredito = text_TarjetaCredito.get()
    textTransporte = text_Transporte.get()
    textObraSocial = text_ObraSocial.get()
    textRecreativos = text_Recreativos.get()
    textIngresoMama = text_IngMama.get()
    textIngresoPapa = text_IngPapa.get()
    savedTime = currentDate + "" +  currentTime
    messagebox.showinfo("Nuevos Datos Ingresados","ok")
    persist(savedTime,textAlquiler,textAuto,textSupermercado,textServicios,textTarjetaCredito,textTransporte,textObraSocial,textRecreativos,textIngresoMama,textIngresoPapa)
    
    
def nuevoIngreso():
    text_IngMama.config(state="normal")
    text_IngPapa.config(state='normal')

def nuevoGasto():
    text_Alquiler.config(state='normal')
    text_Auto.config(state='normal')
    text_Supermercado.config(state='normal')
    text_Servicios.config(state='normal')
    text_TarjetaCredito.config(state='normal')
    text_Transporte.config(state='normal')
    text_ObraSocial.config(state='normal')
    text_Recreativos.config(state='normal')
    
def deleteGastos():
    text_Alquiler.delete(0, "end")
    text_Auto.delete(0, "end")
    text_Supermercado.delete(0, "end")
    text_Servicios.delete(0, "end")
    text_TarjetaCredito.delete(0, "end")
    text_Transporte.delete(0, "end")
    text_ObraSocial.delete(0, "end")
    text_Recreativos.delete(0, "end")
    
def deleteIngresos():
    text_IngMama.delete(0, "end")
    text_IngPapa.delete(0, "end")
    

imagen=PhotoImage(file="economia1.png")
label_imagen=Label(ventana,image=imagen)
label_imagen.place(x = 0, y = 0)
label_imagen.pack()

label_EconomiaFamiliar=Label(ventana,text="Economia Familiar")
label_EconomiaFamiliar.pack()
label_EconomiaFamiliar.config(fg="#585858",bg="white", fon = ("Goudy Stout",12))
label_EconomiaFamiliar.place(x = 350, y =0)

label_IngresoMama=Label(ventana,text="Ingresos Mama --> ")
label_IngresoMama.pack()
label_IngresoMama.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_IngresoMama.place(x=170, y = 100)


label_IngresoPapa=Label(ventana,text="Ingresos Papa --> ")
label_IngresoPapa.pack()
label_IngresoPapa.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_IngresoPapa.place(x=170, y = 150)

label_Ingresos=Label(ventana,text="INGRESOS ")
label_Ingresos.pack()
label_Ingresos.config(fg="white",bg="#0B3B24", fon = ("Century Gothic",15))
label_Ingresos.place(x = 20, y = 130)

label_Gastos=Label(ventana,text="GASTOS ")
label_Gastos.pack()
label_Gastos.config(fg="white",bg="#0B3B24", fon = ("Century Gothic",15))
label_Gastos.place(x = 150, y = 130)


label_Alquiler=Label(ventana,text="Alquiler -->")
label_Alquiler.pack()
label_Alquiler.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_Alquiler.place(x=400, y = 100)

label_Auto=Label(ventana,text="Automovil --> ")
label_Auto.pack()
label_Auto.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_Auto.place(x=400, y = 150)

label_Supermercado=Label(ventana,text="Supermercado --> ")
label_Supermercado.pack()
label_Supermercado.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_Supermercado.place(x=400, y = 200)

label_Servicios=Label(ventana,text="Servicios --> ")
label_Servicios.pack()
label_Servicios.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_Servicios.place(x=400, y = 250)

label_TarjetaCredito=Label(ventana,text="Tarjeta de Credito --> ")
label_TarjetaCredito.pack()
label_TarjetaCredito.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_TarjetaCredito.place(x=400, y = 300)

label_Transporte=Label(ventana,text="Transporte --> ")
label_Transporte.pack()
label_Transporte.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_Transporte.place(x=400, y = 350)

label_ObraSocial=Label(ventana,text="Obra Social --> ")
label_ObraSocial.pack()
label_ObraSocial.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_ObraSocial.place(x=400, y = 400)


label_Recreativos=Label(ventana,text="Recreativos --> ")
label_Recreativos.pack()
label_Recreativos.config(fg="black",bg="white",fon = ("Agency FB", 15))
label_Recreativos.place(x=400, y = 450)


text_IngMama=Entry(ventana)
text_IngMama.config(state='readonly')
text_IngMama.place(x=300, y = 105)

text_IngPapa=Entry(ventana)
text_IngPapa.config(state='readonly')
text_IngPapa.place(x=300, y = 155)

text_Alquiler=Entry(ventana)
text_Alquiler.config(state='readonly')
text_Alquiler.place(x=550, y = 105)

text_Auto=Entry(ventana)
text_Auto.config(state='readonly')
text_Auto.place(x=550, y = 155)

text_Supermercado=Entry(ventana)
text_Supermercado.config(state='readonly')
text_Supermercado.place(x=550, y = 205)

text_Servicios=Entry(ventana)
text_Servicios.config(state='readonly')
text_Servicios.place(x=550, y = 255)

text_TarjetaCredito=Entry(ventana)
text_TarjetaCredito.config(state='readonly')
text_TarjetaCredito.place(x=550, y = 305)

text_Transporte=Entry(ventana)
text_Transporte.config(state='readonly')
text_Transporte.place(x=550, y = 355)

text_ObraSocial=Entry(ventana)
text_ObraSocial.config(state='readonly')
text_ObraSocial.place(x=550, y = 405)

text_Recreativos=Entry(ventana)
text_Recreativos.config(state='readonly')
text_Recreativos.place(x=550, y = 455)

botonNuevoGasto=Button(ventana, text="Nuevos Gastos",command = nuevoGasto)
botonNuevoGasto.place(x = 300, y = 550)
botonNuevoGasto.config(bg="#2EFEF7", fg= "black")

botonGuardarGastos=Button(ventana,text="Guardar Gastos",command=enviarDatos)
botonGuardarGastos.place(x = 450, y = 550)
botonGuardarGastos.config(bg="#848484", fg= "black")

botonNuevoIngreso=Button(ventana, text="Nuevo Ingreso",  command = nuevoIngreso)
botonNuevoIngreso.place(x = 200, y = 250)
botonNuevoIngreso.config(bg="#2EFEF7", fg= "black")

botonGuardarIngresos=Button(ventana,text="Guardar Ingresos",command=enviarDatos)
botonGuardarIngresos.place(x = 350, y = 250)
botonGuardarIngresos.config(bg="#848484", fg= "black")

botonBorrarIngresos=Button(ventana,text="Borrar Ingresos",command=deleteIngresos)
botonBorrarIngresos.place(x=450, y= 250 )
botonBorrarIngresos.config(bg="#FF0000", fg= "black")

botonBorrarGastos=Button(ventana,text="Borrar Gastos",command=deleteGastos) 
botonBorrarGastos.place (x = 600, y = 550)
botonBorrarGastos.config(bg="#FF0000", fg= "black")


ventana.mainloop()