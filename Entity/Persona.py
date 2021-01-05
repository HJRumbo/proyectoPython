class Persona:
    """description of class"""
    def __init__(self, nombre, sexo, edad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.pulsaciones = 0.0

    def calcularpulsacion(self):
        if self.sexo.upper() == "F":
            self.pulsaciones = (220 - self.edad)/10
        elif self.sexo.upper() == "M":
            self.pulsaciones = (210 - self.edad)/10
