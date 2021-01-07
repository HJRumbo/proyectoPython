from DAL.PersonaRepository import PersonaRpository


class PersonaService(object):
    """description of class"""

    personaRepository = PersonaRpository()

    def guardarPersona(self, persona):
        try:
            if self.personaRepository.buscarXIdentificacion(persona.identificacion) is None:
                self.personaRepository.guardarPersona(persona)
                return "Persona guaradada correctamente. "
            return "La persona con la identificación " + persona.identificacion + " ya se encuentra registrada. "
        except:
            return "Error al guardar la persona. "

    def consultarTodos(self):
        personas = self.personaRepository.consultarTodos()
        return personas

    def buscarXIdentificacion(self, identificacion):
        persona = self.personaRepository.buscarXIdentificacion(identificacion)
        return persona

    def eliminar(self, identificacion):
        try:
            self.personaRepository.eliminar(identificacion)
            return "Perosna eliminada correctamente. "
        except:
            return "Error al momento de eliminar a la persona. "

    def editar(self, persona):
        try:
            self.personaRepository.editar(persona)
            return "Perosna modificada correctamente. "
        except:
            return "Error al momento de modificar a la persona. "
