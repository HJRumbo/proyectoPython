from array import array

from Entity import Persona


class PersonaRpository(object):
    """description of class"""

    file = "Persona.txt"
    personas = []

    def guardarPersona(self, persona):
        """description of method"""
        f = open(self.file, 'a')
        f.write(persona.nombre + ';' + str(persona.edad) + ';' + persona.sexo + ';' + str(persona.pulsaciones))
        f.write("\n")
        f.close()

    def consultarTodos(self):
        """description of method"""
        f = open(self.file, 'r')
        for line in f.readlines():

            persona = Persona

            separador = ";"
            separado = line.split(separador)

            persona.nombre = separado[0]
            persona.edad = separado[1]
            persona.sexo = separado[2]
            persona.pulsaciones = separado[3]

            self.personas[len(self.personas):] = [persona]
        f.close()
        return self.personas

    def mapear(self, line):
        separador = ";"
        separado = line.split(separador)

        persona = Persona

        persona.nombre = separado[0]
        persona.edad = separado[1]
        persona.sexo = separado[2]
        persona.pulsaciones = separado[3]

        return persona

    def buscarXNombre(self, nombre):
        personas = self.consultarTodos()
        for item in personas:
            if item.nombre == nombre:
                return item
        return None