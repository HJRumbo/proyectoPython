from DAL.PersonaRepository import PersonaRpository


class PersonaService(object):
    """MANEJO DE ARCHIVO DE TEXTO"""

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

    """MANEJ0 DE BASE DE DATOS (SQLite)"""

    def guardarPersonaBD(self, persona):
        try:

            self.personaRepository.guardarPersonaBD(persona)
            return "Persona guaradada correctamente. "

        except:
            return "Error al guardar la persona. "

    def consultarTodosBD(self):
        personas = self.personaRepository.consultarTodosBD()
        return personas

    def buscarXIdentificacionBD(self, identificacion):
        persona = self.personaRepository.buscarXIdentificacionBD(identificacion)
        return persona

    def eliminarBD(self, identificacion):
        self.personaRepository.eliminarBD(identificacion)
        return "Perosna eliminada correctamente. "

    def editarBD(self, persona):
        try:
            self.personaRepository.editarBD(persona)
            return "Perosna modificada correctamente. "
        except:
            return "Error al momento de modificar a la persona. "
