import sqlite3
from array import array
from os import remove
import os.path as path
from tkinter import messagebox

from DAL.ConnectionManager import ConnectionManager
from Entity.Persona import Persona


class PersonaRpository(object):
    """MANEJO DE ARCHIVO DE TEXTO"""

    def __init__(self):
        self.conexion = self.connectionManager.crear_conexion(self.base_datos)
        self.connectionManager.crear_tabla(self.conexion, self.tabla)

    file = "Persona.txt"
    personas = []
    connectionManager = ConnectionManager()
    base_datos = 'pulsacion.db'
    tabla = """Create table if not exists persona
    (identificacion text primary key, nombre text, sexo text, edad int, pulsaciones double)"""

    def guardarPersona(self, persona):
        """description of method"""
        f = open(self.file, 'a')
        f.write(
            persona.identificacion + ';' + persona.nombre + ';' + str(persona.edad) + ';' + persona.sexo + ';' + str(
                persona.pulsaciones))
        f.write("\n")
        f.close()

    def consultarTodos(self):
        """description of method"""
        if path.exists(self.file):
            self.personas.clear()
            f = open(self.file, 'r')
            for line in f.readlines():
                separador = ";"
                separado = line.split(separador)

                identificacion = separado[0]
                nombre = separado[1]
                edad = separado[2]
                sexo = separado[3]

                persona = Persona(identificacion, nombre, sexo, float(edad))
                persona.calcularpulsacion()

                self.personas[len(self.personas):] = [persona]
            f.close()
            return self.personas
        else:
            return None

    def mapear(self, line):
        separador = ";"
        separado = line.split(separador)

        persona = Persona

        persona.nombre = separado[0]
        persona.edad = separado[1]
        persona.sexo = separado[2]
        persona.pulsaciones = separado[3]

        return persona

    def buscarXIdentificacion(self, identificacion):
        personas = self.consultarTodos()
        for item in personas:
            if item.identificacion == identificacion:
                return item
        return None

    def eliminar(self, identificacion):
        personas = self.consultarTodos()
        remove(self.file)
        for item in personas:
            if item.identificacion != identificacion:
                self.guardarPersona(item)

    def editar(self, persona):
        personas = self.consultarTodos()
        remove(self.file)
        for item in personas:
            if item.identificacion != persona.identificacion:
                self.guardarPersona(item)
            else:
                self.guardarPersona(persona)

    """MANEJ0 DE BASE DE DATOS (SQLite)"""

    def guardarPersonaBD(self, persona):
        """description of method"""
        sql = "INSERT INTO persona(identificacion, nombre, sexo, edad, pulsaciones) VALUES (?,?,?,?,?)"
        parametros = (persona.identificacion, persona.nombre, persona.sexo, persona.edad, persona.pulsaciones)
        cursor = self.conexion.cursor()
        result = cursor.execute(sql, parametros)
        self.conexion.commit()
        cursor.close()

    def consultarTodosBD(self):
        """description of method"""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM persona")
        personas = cursor.fetchall()
        for person in personas:
            identificacion = person[0]
            nombre = person[1]
            sexo = person[2]
            edad = person[3]

            persona = Persona(identificacion, nombre, sexo, float(edad))
            persona.calcularpulsacion()

            self.personas.append(persona)
        return self.personas
        cursor.close()

    def buscarXIdentificacionBD(self, identificacion):
        personas = self.consultarTodosBD()
        for item in personas:
            if item.identificacion == identificacion:
                return item
        return None

    def eliminarBD(self, identificacion):
        cursor = self.conexion.cursor()

        sql = "DELETE FROM persona WHERE identificacion = ?"
        cursor.execute(sql, (identificacion,))

        self.conexion.commit()

    def editarBD(self, persona):
        cursor = self.conexion.cursor()

        sql = "UPDATE persona SET nombre = ?, sexo = ?, edad = ?, pulsaciones = ? WHERE identificacion = ?"
        parametros = (persona.nombre, persona.sexo, persona.edad, persona.pulsaciones, persona.identificacion)
        cursor.execute(sql, parametros)

        self.conexion.commit()