import tkinter as tk
from tkinter import * 
from tkinter.constants import X



root = tk.Tk()
root.title("Facial")
root.iconbitmap("loogo.ico")

logo = tk.PhotoImage(file="logo.png")

w1 = tk.Label(root,width=400,height=300, image=logo).pack()

miFrame =Frame(root, width=500,height=400)
miFrame.pack()

milogo=Entry(miFrame)
milogo=PhotoImage(file="logo.png")
milogo=Label(miFrame, image=milogo).place(x=100, y=200)

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)
cuadroApellido.config(justify="center")

cuadroFacultad=Entry(miFrame)
cuadroFacultad.grid(row=2, column=1, padx=10, pady=10)
cuadroFacultad.config(justify="center")

cuadroIngreso=Entry(miFrame)
cuadroIngreso.grid(row=3, column=1, padx=10, pady=10)
cuadroIngreso.config(justify="center")

cuadroNombre =Label(miFrame, text="Nombre:").grid(row=0, column=0)
cuadroApellido =Label(miFrame, text="Apellido:").grid(row=1, column=0)
cuadroFacultad =Label(miFrame, text="Facultad:").grid(row=2, column=0)
cuadroIngreso =Label(miFrame, text="Ingreso:").grid(row=3, column=0)

explanation = """Facial."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(fill="x",padx=10, pady=10)


root.mainloop()
