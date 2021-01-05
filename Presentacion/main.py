# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox
import tkinter as tk

from BLL.PersonaService import PersonaService
from Entity.Persona import *

personaService = PersonaService()


def ventana():
    window = Tk()
    window.title("Pulsaciones")
    lbl = Label(window, text="Nombre")
    lbl.grid(column=0, row=0, padx=10)
    txt = Entry(window, width=20)
    txt.grid(column=4, row=0, padx=30, pady=5)
    txt.focus()
    lblS = Label(window, text="Sexo")
    lblS.grid(column=0, row=3)
    combo = Combobox(window, width=17)
    combo['values'] = ("F", "M")
    combo.current(1)  # set the selected item.
    combo.grid(column=4, row=3, padx=30, pady=5)
    lblE = Label(window, text="Edad")
    lblE.grid(column=0, row=6)
    txtE = Entry(window, width=20)
    txtE.grid(column=4, row=6, padx=30, pady=5)
    lblP = Label(window, text="Pulsaciones")
    lblP.grid(column=0, row=9, padx=10)
    lblPr = Label(window)
    lblPr.grid(column=4, row=9, padx=10)

    def clicked():
        nombre = txt.get()
        sexo = combo.get()
        edad = float(txtE.get())
        persona = Persona(nombre, sexo, edad)
        persona.calcularpulsacion()
        lblPr.configure(text=str(persona.pulsaciones))
        mensaje = personaService.guardarPersona(persona)
        messagebox.showinfo("Mensaje", mensaje)

    btn = Button(window, text="Click Me", command=clicked)
    btn.grid(column=10, row=10)

    btnC = Button(window, text="Consultar", command=createnewWindow)
    btnC.grid(column=0, row=30)

    window.geometry('350x200')
    window.mainloop()


def createnewWindow():
    newWindow = tk.Toplevel()
    newWindow.title("Consulta")
    treeView = ttk.Treeview(newWindow)
    treeView.grid(column=0, row=15, padx=20)
    treeView["columns"] = ["Nombre", "Edad", "Sexo", "Pulsaciones"]
    treeView["show"] = "headings"
    treeView.heading("Nombre", text="Nombre")
    treeView.heading("Edad", text="Edad")
    treeView.heading("Sexo", text="Sexo")
    treeView.heading("Pulsaciones", text="Pulsaciones")

    personas = personaService.consultarTodos()
    c=0
    for item in personas:
        treeView.insert("", c, iid=None, values=(item.nombre, item.edad, item.sexo, item.pulsaciones))
        c=c+1


def main():
    ventana()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
