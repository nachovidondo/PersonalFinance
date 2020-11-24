from tkinter import*
from datetime import datetime
from tkinter.ttk import Treeview
from consulta import *
import time
import locale
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.ttk as ttk

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
    
def showIngresos():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Ingresos")
        data = (row for row in cursor.fetchall())

        ventana = tk.Tk()
        table = Table(ventana, headings=('Fecha', 'Ingreso Mama','Ingreso Papa'), rows=data)
        table.pack(expand=tk.YES, fill=tk.BOTH)

def showGastosFijos():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM 'Gastos Fijos' ")
        data = (row for row in cursor.fetchall())
        ventana = tk.Tk()
        table= ttk.Treeview(ventana)
        table = Table(ventana, headings=('Fecha', 'Alquiler','Servicios','Tarjeta de Credito','Obra Social'), rows=data)
        table.pack(expand=tk.YES, fill=tk.BOTH)
        table.grid(row=0,column=1,rowspan=5)
        
def showGastosVariables():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM 'Gastos Variables' ")
        data = (row for row in cursor.fetchall())

        ventana = tk.Tk()
        table= ttk.Treeview(ventana)
        table = Table(ventana, headings=('Fecha','Automovil','Supermercado','Transporte','Recreativos'), rows=data)
        table.pack(expand=tk.YES, fill=tk.BOTH)
        table.grid(row=0,column=1,rowspan=5)
        

imagen=PhotoImage(file="economia1.png")
label_imagen=Label(ventana,image=imagen)
label_imagen.place(x = 0, y = 0)
label_imagen.pack()

label_EconomiaFamiliar=Label(ventana,text="Economia Familiar")
label_EconomiaFamiliar.pack()
label_EconomiaFamiliar.config(fg="black",bg="white", fon = ("Century Gothic",25))
label_EconomiaFamiliar.place(x = 350, y =0)

label_CurrentDate = Label(ventana,text=currentDate) 
label_CurrentDate.pack()
label_CurrentDate.config(fg="black",bg="white", fon = ("Century Gothic", 15))
label_CurrentDate.place(x = 900, y =0)

label_IngresoMama=Label(ventana,text="Ingresos Mama")
label_IngresoMama.pack()
label_IngresoMama.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_IngresoMama.place(x=150, y = 100)


label_IngresoPapa=Label(ventana,text="Ingresos Papa")
label_IngresoPapa.pack()
label_IngresoPapa.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_IngresoPapa.place(x=150, y = 150)

label_Ingresos=Label(ventana,text="INGRESOS ")
label_Ingresos.pack()
label_Ingresos.config(fg="white",bg="black", fon = ("Century Gothic",10))
label_Ingresos.place(x = 10, y = 120)

label_GastosFijos=Label(ventana,text="GASTOS\nFIJOS ")
label_GastosFijos.pack()
label_GastosFijos.config(fg= "white",bg="black", fon = ("Century Gothic",10)) 

label_GastosVariables=Label(ventana,text="GASTOS\nVARIABLES ")
label_GastosVariables.pack()
label_GastosVariables.config(fg= "white",bg="black", fon = ("Century Gothic",10))
label_GastosVariables.place(x = 370, y = 350)

label_Alquiler=Label(ventana,text="Alquiler ")
label_Alquiler.pack()
label_Alquiler.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_Alquiler.place(x=100, y = 300)

label_Auto=Label(ventana,text="Automovil")
label_Auto.pack()
label_Auto.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_Auto.place(x=470, y = 400)

label_Supermercado=Label(ventana,text="Supermercado")
label_Supermercado.pack()
label_Supermercado.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_Supermercado.place(x=460, y = 300)

label_Servicios=Label(ventana,text="Servicios")
label_Servicios.pack()
label_Servicios.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_Servicios.place(x=100, y = 400)

label_TarjetaCredito=Label(ventana,text="Tarjeta de Credito")
label_TarjetaCredito.pack()
label_TarjetaCredito.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_TarjetaCredito.place(x=80, y = 450)

label_Transporte=Label(ventana,text="Transporte")
label_Transporte.pack()
label_Transporte.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_Transporte.place(x=470, y = 350)

label_ObraSocial=Label(ventana,text="Obra Social")
label_ObraSocial.pack()
label_ObraSocial.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_ObraSocial.place(x=100, y = 350)


label_Recreativos=Label(ventana,text="Recreativos")
label_Recreativos.pack()
label_Recreativos.config(fg="black",bg="white",fon = ("Century Gothic", 10))
label_Recreativos.place(x=470, y = 450)


text_IngMama=Entry(ventana)
text_IngMama.config(state='readonly')
text_IngMama.place(x=270, y = 105)

text_IngPapa=Entry(ventana)
text_IngPapa.config(state='readonly')
text_IngPapa.place(x=270, y = 155)

text_Alquiler=Entry(ventana)
text_Alquiler.config(state='readonly')
text_Alquiler.place(x=205, y = 305)

text_Auto=Entry(ventana)
text_Auto.config(state='readonly')
text_Auto.place(x=565, y = 405)

text_Supermercado=Entry(ventana)
text_Supermercado.config(state='readonly')
text_Supermercado.place(x=565, y = 305)

text_Servicios=Entry(ventana)
text_Servicios.config(state='readonly')
text_Servicios.place(x=205, y = 405)

text_TarjetaCredito=Entry(ventana)
text_TarjetaCredito.config(state='readonly')
text_TarjetaCredito.place(x=205, y = 455)

text_Transporte=Entry(ventana)
text_Transporte.config(state='readonly')
text_Transporte.place(x=565, y = 355)

text_ObraSocial=Entry(ventana)
text_ObraSocial.config(state='readonly')
text_ObraSocial.place(x=205, y = 355)

text_Recreativos=Entry(ventana)
text_Recreativos.config(state='readonly')
text_Recreativos.place(x=565, y = 455)

botonNuevoGasto=Button(ventana, text="Nuevos  Gastos",command = nuevoGasto)
botonNuevoGasto.place(x = 120, y = 520)
botonNuevoGasto.config(bg="white", fg= "black")

botonGuardarGastosFijos=Button(ventana,text="Guardar Gastos Fijos",command=enviarDatos)
botonGuardarGastosFijos.place(x = 250, y = 520)
botonGuardarGastosFijos.config(bg="white", fg= "black")

botonGuardarGastosVariables=Button(ventana,text="Guardar Gastos Variables",command=enviarDatos)
botonGuardarGastosVariables.place(x = 520, y = 520)
botonGuardarGastosVariables.config(bg="white", fg= "black")

botonBorrarGastos=Button(ventana,text="Borrar  Gastos",command=deleteGastos) 
botonBorrarGastos.place (x = 400, y = 520)
botonBorrarGastos.config(bg="white", fg= "black")

botonNuevoIngreso=Button(ventana, text="Nuevo Ingreso",  command = nuevoIngreso)
botonNuevoIngreso.place(x = 450, y = 80)
botonNuevoIngreso.config(bg="white", fg= "black")

botonGuardarIngresos=Button(ventana,text="Guardar Ingresos",command=enviarDatos)
botonGuardarIngresos.place(x = 450, y = 130)
botonGuardarIngresos.config(bg="white", fg= "black")

botonBorrarIngresos=Button(ventana,text="Borrar Ingresos",command=deleteIngresos)
botonBorrarIngresos.place(x=450, y= 180 )
botonBorrarIngresos.config(bg="white", fg= "black")

menubar=Menu(ventana)
ventana.config(menu=menubar)
Mostrarmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Menu ", menu= Mostrarmenu)

Mostrarmenu.add_command(label="Abrir Ingresos",command=showIngresos)
Mostrarmenu.add_separator()
Mostrarmenu.add_command(label="Abrir Gastos Fijos",command=showGastosFijos)
Mostrarmenu.add_separator()
Mostrarmenu.add_command(label="Abrir Gastos Variables",command=showGastosVariables)
Mostrarmenu.add_separator()

  #Clase para crear Tablas
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
  
  


ventana.mainloop()
