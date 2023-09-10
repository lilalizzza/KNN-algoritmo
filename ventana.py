import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
#import pandas as pd
#import numpy as np


#------------------------INTERFAZ--------------------------

#------Ventana-------
ventana = tk.Tk()
ventana.title("Prueba ventana")
ventana.geometry("1000x1000")
ventana.config(bg="#CD4040")
#ventana.resizable(0,0)

#--------Label-------
nombre = tk.Label(ventana, text="   KNN ALGORITMO          ")
nombre.config(font=("Arial", 26), bg="red")
nombre.pack()
#-----Crear un scrollbar---------
scrollbar = tk.Scrollbar(ventana)
scrollbar.pack(fill=tk.Y)
scrollbar.pack_configure(side=tk.LEFT)

#------Crear un widget de texto----------
texto = tk.Text(ventana, yscrollcommand=scrollbar.set)
texto.pack(fill=tk.BOTH, expand=True)
texto.pack_configure(side=tk.LEFT)
texto.pack()
#-----------Crear un widget para Valor de K---------
entry = tk.Entry(ventana)
entry.config(bg="white")    
entry.pack()


# Muestra las opciones de K
#combo = tk.Combobox(ventana, values=["Opción 1", "Opción 2", "Opción 3"])
#ombo.place(x=50, y=50)
#combo.pack()
#--------def iniciar(self):
#--    self.btn_seleccionar_archivo = tk.Button(self, text='Seleccionar archivo')
#--    self.btn_seleccionar_archivo['command'] = self.seleccionar_archivo 
#--    self.btn_seleccionar_archivo.pack()
#--    self.txa_contenido_archivo.pack()



# Asignar un manejador de eventos al botón
def registrar():
    global value  
    value = entry.get()
    print(value)

























#--------------    BOTONES    -----------------------
# BOTON PARA SELECCIONAR UN ARCHIVO
def selecc_Archivo():
    archivo = askopenfile(mode='r', filetypes=[('Archivo de texto', '*.csv')])
    if archivo is not None:
        contenido = archivo.read()
     # Insertar el contenido del archivo en el widget de texto
        texto.insert(tk.END, contenido)
    # Configurar el valor máximo del scrollbar
        scrollbar.config(max=len(contenido))
        archivo.close()

# ABRE EL ARCHIVO  CON LA BASE DE DATOS ORIGINAL    
def abrir_archivo():
   archivo = open("golf.csv", encoding="utf-8")
   texto = archivo.read()
   print(texto)
   archivo.close()



# Crear un widget Button
button = tk.Button(ventana, text="Registrar", command=registrar,  bg="white", fg="red")
button.place(x=355, y=150, height=75, width=150)
button.pack()


boton = tk.Button(ventana, text="Mostar base de datos", command = abrir_archivo, bg="white", fg="red")
boton.pack()
boton.place(x=700, y=80, height=75, width=150)

boton1 = tk.Button(ventana, text="Seleccionar Archivo", command = selecc_Archivo, bg="white", fg="red")
boton1.pack()
boton1.place(x=700, y=300, height=75, width=150)

boton2 = tk.Button(ventana, text="BOTON ", command = selecc_Archivo, bg="white", fg="red")
boton2.pack()
boton2.place(x=700, y=190, height=75, width=150)




ventana.mainloop()
