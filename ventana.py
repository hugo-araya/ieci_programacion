from tkinter import *
ventana = Tk()
ventana.title('Primera ventana')
ventana_2 = Tk()
ventana_2.title('Segunda ventana')
label1 = Label(ventana,text="Nombre")
label1.grid(row=1,column=1)
texto_1 = StringVar()
entrada_1 = Entry(ventana,textvariable=texto_1)
entrada_1.grid(row=1,column=2)
label2 = Label(ventana,text="Apellido")
label2.grid(row=2,column=1)
texto_2 = StringVar()
entrada_2 = Entry(ventana,textvariable=texto_2)
entrada_2.grid(row=2,column=2)
label3 = Label(ventana,text="Email")
label3.grid(row=3,column=1)
texto_3 = StringVar()
entrada_3 = Entry(ventana,textvariable=texto_3)
entrada_3.grid(row=3,column=2)
btn_finalizar = Button(ventana,text="Finalizar", command = quit)
btn_finalizar.grid(row=4,column=2)
ventana.mainloop()