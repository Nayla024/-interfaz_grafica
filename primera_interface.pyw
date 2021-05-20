from tkinter import * 

# # raiz.resizable(0,0) para que se quede el tamaño y no se modifique
# raiz.geometry ("1050x550") #tamaño por defecto
# # raiz.config(bg="") cambiar el color de fondo

#fill="x" se redimenciona el frame expaniendo horizontal
# fill="y",expand="True" se redimenciona el frame expaniendo verticalmente
#fill="both",expand="True" se redimenciona el frame expaniendo ambos sentidos
#stiky izquierda derecha arriba abajo ...etc (con puntos cardinales: w-n-s-e) Video IV. 

root=Tk()
root.title("Facial")
root.iconbitmap("loogo.ico")

# miFrameImage=Frame(root)
# miFrameImage.pack(fill="y")

# milogo=PhotoImage(file="logo.png")
# milogo=Label(miFrameImage, image=milogo).place(x=100, y=200)

# miFramecamara=Frame(root)
# miFramecamara.pack(side="left")

miFrame =Frame(root, width=500,height=400)
miFrame.pack()

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

root.mainloop()