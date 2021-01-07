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
    lblI = Label(window, text="Identificacion")
    lblI.grid(column=0, row=0, padx=10)
    txtI = Entry(window, width=20)
    txtI.grid(column=4, row=0, padx=30, pady=5)
    txtI.focus()

    def limpiar():
        txtI.set("")
        txtI.focus()
        txt.set("")
        combo.set("M")
        txtE.insert(0, "")
        lblPr.configure(text=str(""))

    def buscarXId():
        persona = personaService.buscarXIdentificacion(txtI.get())
        txt.insert(0, persona.nombre)
        combo.set(persona.sexo)
        txtE.insert(0, persona.edad)
        lblPr.configure(text=str(persona.pulsaciones))

    btnB = Button(window, text="Buscar", command=buscarXId)
    btnB.grid(column=5, row=0, pady=5)
    lbl = Label(window, text="Nombre")
    lbl.grid(column=0, row=3, padx=10)
    txt = Entry(window, width=20)
    txt.grid(column=4, row=3, padx=30, pady=5)
    lblS = Label(window, text="Sexo")
    lblS.grid(column=0, row=6)
    combo = Combobox(window, width=17, state="readonly")
    combo['values'] = ("F", "M")
    combo.current(1)  # set the selected item.
    combo.grid(column=4, row=6, padx=30, pady=5)
    lblE = Label(window, text="Edad")
    lblE.grid(column=0, row=9)
    txtE = Entry(window, width=20)
    txtE.grid(column=4, row=9, padx=30, pady=5)
    lblP = Label(window, text="Pulsaciones")
    lblP.grid(column=0, row=12, padx=10)
    lblPr = Label(window)
    lblPr.grid(column=4, row=12, padx=10)

    def clicked():
        try:
            identificacion = txtI.get()
            nombre = txt.get()
            sexo = combo.get()
            edad = float(txtE.get())
            persona = Persona(identificacion, nombre, sexo, edad)
            persona.calcularpulsacion()
            lblPr.configure(text=str(persona.pulsaciones))
            mensaje = personaService.guardarPersona(persona)
        except:
            mensaje = "Error al momento de guardar los datos. Por favor, verifique que llenó todos los campos. "
        messagebox.showinfo("Mensaje", mensaje)

    btn = Button(window, text="Guardar", command=clicked)
    btn.grid(column=5, row=14)

    btnC = Button(window, text="Consultar", command=createnewWindow)
    btnC.grid(column=0, row=16, pady=10)

    def eliminar():
        mensaje = personaService.eliminar(txtI.get())
        messagebox.showinfo("Mensaje", mensaje)

    btnEl = Button(window, text="Eliminar", command=eliminar)
    btnEl.grid(column=4, row=16, pady=10)

    def editar():
        identificacion = txtI.get()
        nombre = txt.get()
        sexo = combo.get()
        edad = float(txtE.get())
        persona = Persona(identificacion, nombre, sexo, edad)
        persona.calcularpulsacion()
        lblPr.configure(text=str(persona.pulsaciones))
        mensaje = personaService.editar(persona)
        messagebox.showinfo("Mensaje", mensaje)

    btnEl = Button(window, text="Editar", command=editar)
    btnEl.grid(column=5, row=16, pady=10)

    window.geometry('350x220')
    window.mainloop()


def createnewWindow():
    personas = personaService.consultarTodos()
    if personas is None:

        messagebox.showinfo("Mensaje", "La lista está vacía.")
    else:
        newWindow = tk.Toplevel()
        newWindow.title("Consulta")
        treeView = ttk.Treeview(newWindow)
        treeView.grid(column=0, row=15, padx=20)
        treeView["columns"] = ["Identificación", "Nombre", "Edad", "Sexo", "Pulsaciones"]
        treeView["show"] = "headings"
        treeView.heading("Identificación", text="Identificación")
        treeView.heading("Nombre", text="Nombre")
        treeView.heading("Edad", text="Edad")
        treeView.heading("Sexo", text="Sexo")
        treeView.heading("Pulsaciones", text="Pulsaciones")

        c = 0
        for item in personas:
            treeView.insert("", c, iid=None, values=(item.identificacion, item.nombre,
                                                     int(item.edad), item.sexo, item.pulsaciones))
            c = c + 1


def main():
    ventana()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
