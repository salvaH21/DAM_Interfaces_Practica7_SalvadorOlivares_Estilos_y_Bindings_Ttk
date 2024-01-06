import tkinter as tk
from tkinter import ttk
import json
import os

listaarchivos = []

def listadodearchivosleer():
    listaarchivos = []
    listadoleer.delete(0,tk.END)
    carpeta = 'C:\\Users\\salva\\Documents\\GitHub2\\archivos_ttk'
    with os.scandir(carpeta) as ficheros:
        for fichero in ficheros:
            if fichero.name.endswith('.json') and fichero.is_file():
                listaarchivos.append(fichero.name)
        print(listaarchivos)
        for archivo in listaarchivos:
            listadoleer.insert(tk.END,archivo)    

def listadodearchivosescribir():
    listaarchivos = []
    listadoescribir.delete(0,tk.END)
    carpeta = 'C:\\Users\\salva\\Documents\\GitHub2\\archivos_ttk'
    with os.scandir(carpeta) as ficheros:
        for fichero in ficheros:
            if fichero.name.endswith('.json') and fichero.is_file():
                listaarchivos.append(fichero.name)
        print(listaarchivos)
        for archivo in listaarchivos:
            listadoescribir.insert(tk.END,archivo) 

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
    botonvolver.pack_forget()
    mensajecreado.pack(padx=10,pady=10)
    botonvolver.pack(padx=10,pady=10)

def aceptar():
    seleccionado = listadoescribir.curselection()
    elemento = listadoescribir.get(seleccionado)
    nombre = campo1.get()
    apellidos = campo2.get()
    edad = campo3.get()
    ciudad = campo4.get()
    print(elemento)
    print(nombre,apellidos,edad,ciudad)
    cadena = {'nombre':nombre,'apellidos':apellidos,'edad':edad,'ciudad':ciudad}
    cadena_json = json.dumps(cadena,indent=1)

    archivo = open(elemento,'a')
    archivo.write(cadena_json + '\n')
    archivo.close()

    campo1.delete(0,tk.END)
    campo2.delete(0,tk.END)
    campo3.delete(0,tk.END)
    campo4.delete(0,tk.END)
    nombrecontacto.pack_forget()
    campo1.pack_forget()
    apellidoscontacto.pack_forget()
    campo2.pack_forget()
    edadcontacto.pack_forget()
    campo3.pack_forget()
    ciudadcontacto.pack_forget()
    campo4.pack_forget()
    botonaceptar.pack_forget()
    botonvolver.pack_forget()
    contactocreado.pack(padx=10,pady=10)
    botonvolver.pack(padx=10,pady=10)

def volver():
    print("Vuelta")
    mensajecreado.pack_forget()
    mensajenuevo.pack_forget()
    mensajeexistente.pack_forget()
    contactocreado.pack_forget()
    nombrearchivo.pack_forget()
    campo1.pack_forget()
    nombrecontacto.pack_forget()
    apellidoscontacto.pack_forget()
    campo2.pack_forget()
    edadcontacto.pack_forget()
    campo3.pack_forget()
    ciudadcontacto.pack_forget()
    campo4.pack_forget()
    botoncrear.pack_forget()
    listadoleer.pack_forget()
    listadoescribir.pack_forget()
    botonaceptar.pack_forget()
    botonvolver.pack_forget()
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
    botonvolver.pack(padx=10,pady=10)

def archivoExistente():
    mensajeinicio.pack_forget()
    desplegable.pack_forget()
    botonsalir.pack_forget()
    listadodearchivosleer()
    mensajeexistente.pack(padx=10,pady=10)
    listadoleer.pack(padx=10,pady=10)
    botonvolver.pack(padx=10,pady=10)

def leerArchivo(evento):
    seleccionado = listadoleer.curselection()
    elemento = listadoleer.get(seleccionado)
    print(elemento)
    archivo = open(elemento,'r')
    print(archivo.read())
    archivo.close()

def escribirEnArchivo():
    print("Escribir")
    mensajeinicio.pack_forget()
    desplegable.pack_forget()
    botonsalir.pack_forget()
    listadodearchivosescribir()
    mensajeexistente.pack(padx=10,pady=10)
    listadoescribir.pack(padx=10,pady=10)
    botonvolver.pack(padx=10,pady=10)

def nuevoContacto(evento):
    seleccionado = listadoescribir.curselection()
    elemento = listadoescribir.get(seleccionado)
    print(elemento)
    mensajeexistente.pack_forget()
    listadoescribir.pack_forget()
    botonvolver.pack_forget()
    nombrecontacto.pack(padx=10,pady=10)
    campo1.pack(padx=10,pady=10)
    apellidoscontacto.pack(padx=10,pady=10)
    campo2.pack(padx=10,pady=10)
    edadcontacto.pack(padx=10,pady=10)
    campo3.pack(padx=10,pady=10)
    ciudadcontacto.pack(padx=10,pady=10)
    campo4.pack(padx=10,pady=10)
    botonaceptar.pack(padx=10,pady=10)
    botonvolver.pack(padx=10,pady=10)


def opcion(evento):
    if desplegable.get() == "Nuevo archivo":
        archivoNuevo()
    elif desplegable.get() == "Abrir archivo existente":
        archivoExistente()
    elif desplegable.get() == "Escribir en archivo":
        escribirEnArchivo()

raiz = tk.Tk()
#ELEMENTOS
mensajeinicio = ttk.Label(raiz,text="Escoge una opción",font=('Arial',12,'bold'))
mensajeinicio.pack(padx=25,pady=25)
mensajenuevo = ttk.Label(raiz,text="NUEVO ARCHIVO",font=('Arial',12,'bold'))
nombrearchivo = ttk.Label(raiz,text="Nombre",style='azul.TLabel')
mensajecreado = ttk.Label(raiz,text="Archivo creado",style='verde.TLabel')
contactocreado = ttk.Label(raiz,text="Contacto añadido",style='verde.TLabel')
mensajeexistente = ttk.Label(raiz,text="Selecciona un archivo:",font=('Arial',12,'bold'))
nombrecontacto = ttk.Label(raiz,text="Nombre",style='azul.TLabel')
apellidoscontacto = ttk.Label(raiz,text="Apellidos",style='azul.TLabel')
edadcontacto = ttk.Label(raiz,text="Edad",style='azul.TLabel')
ciudadcontacto = ttk.Label(raiz,text="Ciudad",style='azul.TLabel')

campo1 = ttk.Entry(raiz)
campo2 = ttk.Entry(raiz)
campo3 = ttk.Entry(raiz)
campo4 = ttk.Entry(raiz)

desplegable = ttk.Combobox(raiz,values=['Nuevo archivo','Abrir archivo existente','Escribir en archivo'])
desplegable.pack(padx=25,pady=25)

botoncrear = ttk.Button(raiz,text="Crear",style='verde.TButton',command=crear)
botonaceptar = ttk.Button(raiz,text="Aceptar",style='verde.TButton',command=aceptar)
botonvolver = ttk.Button(raiz,text="Volver",style='azul.TButton',command=volver)
botonsalir = ttk.Button(raiz,text="Salir",style='rojo.TButton',command=salir)
botonsalir.pack(padx=25,pady=25)

listadoleer = tk.Listbox(raiz)
listadoescribir = tk.Listbox(raiz)

#BINDINGS
listadoleer.bind('<ButtonRelease-1>',leerArchivo)
listadoescribir.bind('<ButtonRelease-1>',nuevoContacto)
desplegable.bind('<<ComboboxSelected>>',opcion)

#ESTILOS
estiloRojo = ttk.Style()
estiloRojo.configure('rojo.TButton',foreground='red')
estiloVerde = ttk.Style()
estiloVerde.configure('verde.TButton',foreground='green')
estiloAzul = ttk.Style()
estiloAzul.configure('azul.TButton',foreground='blue')
estiloLabelVerde = ttk.Style()
estiloLabelVerde.configure('verde.TLabel',foreground='green',background='yellow',font=('Verdana',12,'bold'))
estiloLabelAzul = ttk.Style()
estiloLabelAzul.configure('azul.TLabel',foreground='blue',font=('Comic Sans MS',10,'bold'))

raiz.geometry("400x450")
raiz.mainloop()
