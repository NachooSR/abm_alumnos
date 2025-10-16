class Persona:
    def __init__(self,nombre,apellido,dni):
        self.nombre= nombre
        self.apellido= apellido
        self.dni =dni
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self,dni):
        if len(dni)<7 or len(dni)>9 or not dni.isdigit():
            raise ValueError("Invalid Format DNI")
        self._dni= dni

        