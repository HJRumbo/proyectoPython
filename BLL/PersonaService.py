from DAL.PersonaRepository import PersonaRpository


class PersonaService(object):
    """description of class"""

    personaRepository = PersonaRpository()

    def guardarPersona(self, persona):
        try:
            self.personaRepository.guardarPersona(persona)
            return "Persona guaradada correctamente. "
        except:
            return "Error al guardar la persona. "

    def consultarTodos(self):
        personas = self.personaRepository.consultarTodos()
        return personas

    def buscarXNombre(self, nombre):
        persona = self.personaRepository.buscarXNombre(nombre)
        return persona
