from array import array
from os import remove
import os.path as path

from Entity.Persona import Persona


class PersonaRpository(object):
    """description of class"""

    file = "Persona.txt"
    personas = []

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