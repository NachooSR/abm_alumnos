from .persona import Persona
from datetime import date,datetime

class Alumno(Persona):
    def __init__(self,id_alumno, id_curso, legajo, nombre, apellido, dni, fecha_nacimiento):
        super().__init__(nombre,apellido,dni)
        self.id_curso= id_curso #Chequear que exista el id del curso
        self.id_alumno = id_alumno #Hardcodeo
        self._legajo= legajo     
        if isinstance(fecha_nacimiento,str):
            self.fecha_nacimiento= datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
        else:
            self.fecha_nacimiento= fecha_nacimiento 

    
    # @classmethod
    # def dni(cls,dni):
    #     if not dni.isdigit():
    #         raise ValueError("DNI must contain only numbers")
    #     if len(dni)>10 or len(dni)<7:
    #         raise ValueError("Length of Dni invalid")         
    
    @property
    def legajo(self):
        return self._legajo
    
    @legajo.setter
    def legajo(self,legajo):
        self._legajo= legajo

    def __repr__(self):
        return (f"{type(self).__name__}(\n"
                f"(id_alumno={self.id_alumno!r},\n"
                f"id_curso={self.id_curso!r},\n"
                f"legajo={self.legajo!r},\n"
                f"nombre={self.nombre!r},\n"
                f"apellido={self.apellido!r},\n" 
                f"dni={self.dni!r},\n"
                f"fecha_nac={self.fecha_nacimiento!r},\n)")
    
    def __str__(self):
        return (
                f"Id_curso:{self.id_curso}\n"
                f"Id_Alumno:{self.id_alumno}\n"
                f"-Alumno: {self.nombre} {self.apellido}\n"
                f"-DNI: {self.dni}\n"
                f"-Legajo: {self.legajo}\n"
                f"-Fecha Nacimiento: {self.fecha_nacimiento}\n"
                )
    def __lt__(self,other):
        #Mas joven "menor"
        return self.fecha_nacimiento > other.fecha_nacimiento
    
    def __eq__(self, other):
        return self.legajo==other.legajo
    
    def __hash__(self):
        return hash(self.legajo)