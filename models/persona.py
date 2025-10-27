class Persona:
    def __init__(self,nombre: str,apellido: str,dni: str):
        """
        Plantilla para crear alumnos
        
        Args:
            nombre(str): nombre de la persona
            apellido(str): apellido de la persona
            dni(str): Documento nacional de identidad
        """
        self.nombre= nombre
        self.apellido= apellido
        self.dni =dni
    
    @property
    def dni(self)-> str:
        """Devuelve el dni de la persona"""
        return self._dni
    
    @dni.setter
    def dni(self,dni: str)->None:
        """
        Valida y asigna el DNI
        Args:
            dni(str): Documento de la persona
        
        Raises:
            ValueError: Si la longitud o el formato son invalidos
        """
        if len(dni)<7 or len(dni)>9 or not dni.isdigit():
            raise ValueError("Invalid Format DNI")
        self._dni= dni

        