from DAL.PersonaRepository import PersonaRpository


class PersonaService(object):
    """description of class"""

    def guardarPersona(self, persona):
        try:
            personaRepository = PersonaRpository()
            personaRepository.guardarPersona(persona)
            return "Persona guaradada correctamente. "
        except:
            return "Error al guardar la persona. "
