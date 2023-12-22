##PRACTICA 7 INTERFACES:
##Realiza una práctica libre en la cual demuestres la aplicación de estilos a uno o varios widgets Ttk,
##y demuestres la lectura y escritura de propiedades y los bindings con respecto a los widgets
##(propongo ejercicio de guardar datos en agenda)
##"Tenéis la capacidad de hacer programas tal que: metas información en campos
##(como por ejemplo una agenda,lo podríais hacer ya, que pongas campos de nombre,
## correo electrónico,teléfono, y que le des a guardar, y que se guarde en un txt)"
import tkinter as tk
from tkinter import ttk

def crear():
    archivo = open("miarchivo.xml",'w')
    print("Archivo creado")
    archivo.close()

def salir():
    raiz.destroy()

def archivoNuevo():
    mensajeinicio.pack_forget()
    desplegable.pack_forget()
    botonsalir.pack_forget()
    mensajenuevo.pack(padx=25,pady=25)
    nombrearchivo.pack(padx=10,pady=10)
    campo1.pack(padx=10,pady=10)
    formatoarchivo.pack(padx=10,pady=10)
    campo2.pack(padx=10,pady=10)
    botoncrear.pack(padx=10,pady=10)
    
    

def opcion(evento):
    print(evento)
    if desplegable.get() == "Nuevo archivo":
        archivoNuevo()
    elif desplegable.get() == "Abrir archivo existente":
        print("Abrir archivo")

raiz = tk.Tk()

mensajeinicio = ttk.Label(raiz,text="Escoge un opción")
mensajeinicio.pack(padx=25,pady=25)

mensajenuevo = ttk.Label(raiz,text="NUEVO ARCHIVO")
nombrearchivo = ttk.Label(raiz,text="Nombre")
formatoarchivo = ttk.Label(raiz,text="Formato")

campo1 = ttk.Entry(raiz)
campo2 = ttk.Entry(raiz)

desplegable = ttk.Combobox(raiz,values=['Nuevo archivo','Abrir archivo existente'])
desplegable.pack(padx=25,pady=25)

botoncrear = ttk.Button(raiz,text="Crear",command=crear)

botonsalir = ttk.Button(raiz,text="Salir",command=salir)
botonsalir.pack(padx=25,pady=25)

desplegable.bind('<<ComboboxSelected>>',opcion)


raiz.geometry("400x400")
raiz.mainloop()
