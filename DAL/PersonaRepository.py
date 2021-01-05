from Entity import Persona


class PersonaRpository(object):
    """description of class"""

    file = "Persona.txt"

    def guardarPersona(self, persona):
        """description of method"""
        personaRepository = PersonaRpository()
        f = open(personaRepository.file, 'a')
        f.write(persona.nombre + ';' + str(persona.edad) + ';' + persona.sexo + ';' + str(persona.pulsaciones))
        f.write("\n")
        f.close()

    def consultarTodos(self):
        """description of method"""
        personaRepository = PersonaRpository()
        f = open(personaRepository.file, 'r')
        lines = []
        for line in f:
            self.mapear(line)
        f.close()

    def mapear(line):
        pass
