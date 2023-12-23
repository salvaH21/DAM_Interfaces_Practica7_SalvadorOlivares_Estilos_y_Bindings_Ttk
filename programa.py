##PRACTICA 7 INTERFACES:
##Realiza una práctica libre en la cual demuestres la aplicación de estilos a uno o varios widgets Ttk,
##y demuestres la lectura y escritura de propiedades y los bindings con respecto a los widgets
##(propongo ejercicio de guardar datos en agenda)
##"Tenéis la capacidad de hacer programas tal que: metas información en campos
##(como por ejemplo una agenda,lo podríais hacer ya, que pongas campos de nombre,
## correo electrónico,teléfono, y que le des a guardar, y que se guarde en un txt)"
import tkinter as tk
from tkinter import ttk
import json
import os

listaarchivos = []

def listadodearchivos():
    listaarchivos = []
    listado.delete(0,tk.END)
    carpeta = 'C:\\Users\\salva\\Documents\\GitHub2\\archivos_ttk'
    with os.scandir(carpeta) as ficheros:
        for fichero in ficheros:
            if fichero.name.endswith('.json') and fichero.is_file():
                listaarchivos.append(fichero.name)
        print(listaarchivos)
        for archivo in listaarchivos:
            listado.insert(tk.END,archivo)    

def crear():
    nombre = campo1.get()
    archivo = open(nombre+'.json','w')
    print("Archivo creado")
    archivo.close()
    campo1.delete(0,tk.END)
    mensajenuevo.pack_forget()
    nombrearchivo.pack_forget()
    campo1.pack_forget()
    botoncrear.pack_forget()
    mensajecreado.pack(padx=10,pady=10)
    botonvolver.pack(padx=10,pady=10)

def volver():
    print("Vuelta")
    mensajecreado.pack_forget()
    mensajeexistente.pack_forget()
    botonvolver.pack_forget()
    listado.pack_forget()
    mensajeinicio.pack(padx=25,pady=25)
    desplegable.pack(padx=25,pady=25)
    botonsalir.pack(padx=25,pady=25)

def salir():
    raiz.destroy()

def archivoNuevo():
    mensajeinicio.pack_forget()
    desplegable.pack_forget()
    botonsalir.pack_forget()
    mensajenuevo.pack(padx=25,pady=25)
    nombrearchivo.pack(padx=10,pady=10)
    campo1.pack(padx=10,pady=10)
    botoncrear.pack(padx=10,pady=10)

def archivoExistente():
    mensajeinicio.pack_forget()
    desplegable.pack_forget()
    botonsalir.pack_forget()
    listadodearchivos()
    mensajeexistente.pack(padx=10,pady=10)
    listado.pack(padx=10,pady=10)
    
    botonvolver.pack(padx=10,pady=10)

def leerArchivo(evento):
    seleccionado = listado.curselection()
    elemento = listado.get(seleccionado)
    print(elemento)
    archivo = open(elemento,'r')
    print(archivo.read())
    archivo.close()

def opcion(evento):
    print(evento)
    if desplegable.get() == "Nuevo archivo":
        archivoNuevo()
    elif desplegable.get() == "Abrir archivo existente":
        archivoExistente()

raiz = tk.Tk()

mensajeinicio = ttk.Label(raiz,text="Escoge un opción")
mensajeinicio.pack(padx=25,pady=25)

mensajenuevo = ttk.Label(raiz,text="NUEVO ARCHIVO")
nombrearchivo = ttk.Label(raiz,text="Nombre")
mensajecreado = ttk.Label(raiz,text="Archivo creado")
mensajeexistente = ttk.Label(raiz,text="Selecciona un archivo:")
#formatoarchivo = ttk.Label(raiz,text="Formato")

campo1 = ttk.Entry(raiz)
#campo2 = ttk.Entry(raiz)

desplegable = ttk.Combobox(raiz,values=['Nuevo archivo','Abrir archivo existente'])
desplegable.pack(padx=25,pady=25)

botoncrear = ttk.Button(raiz,text="Crear",command=crear)
botonvolver = ttk.Button(raiz,text="Volver",command=volver)

##botonprueba = ttk.Button(raiz,text="Prueba",command=pulsar)
##botonprueba.pack(padx=25,pady=25)

botonsalir = ttk.Button(raiz,text="Salir",command=salir)
botonsalir.pack(padx=25,pady=25)

listado = tk.Listbox(raiz)

listado.bind('<ButtonRelease-1>',leerArchivo)
desplegable.bind('<<ComboboxSelected>>',opcion)

raiz.geometry("400x400")
raiz.mainloop()
