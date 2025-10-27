from .persona import Persona
from datetime import date,datetime

class Alumno(Persona):
    """
    Clase para modelar un alumno dentro del sistema
    """
    def __init__(self,id_alumno: int, id_curso: int, legajo: str, nombre: str, apellido: str, dni: str, fecha_nacimiento: str|date):
        """
        Inicializa una instancia del alumno

        Args:
            id_alumno(int): Identificador unico
            id_curso(int): Identificador del curso asociado
            legajo(str): Codigo interno del alumno
            nombre(str): Nombre del alumno
            apellido(str): Apellido del alumno
            dni(str): Documento nacional de identidad
            fecha_nacimiento(str | date): Fecha de nacimiento (como string 'dd/mm/yyyy' o date)
        """
        super().__init__(nombre,apellido,dni)
        self.id_curso= id_curso #Chequear que exista el id del curso
        self.id_alumno = id_alumno #Hardcodeo
        self._legajo= legajo     
        if isinstance(fecha_nacimiento,str):
            self.fecha_nacimiento= datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
        else:
            self.fecha_nacimiento= fecha_nacimiento       
    
    @property
    def legajo(self)-> str:
        """Devuelve el legajo de un alumno"""
        return self._legajo
    
    @legajo.setter
    def legajo(self,legajo: int)-> None:
        """Actualiza el legajo de un alumno"""
        self._legajo= legajo

    def __repr__(self)-> str:
        """Representa a un alumno tecnicamente (Debugging)"""
        return (f"{type(self).__name__}(\n"
                f"(id_alumno={self.id_alumno!r},\n"
                f"id_curso={self.id_curso!r},\n"
                f"legajo={self.legajo!r},\n"
                f"nombre={self.nombre!r},\n"
                f"apellido={self.apellido!r},\n" 
                f"dni={self.dni!r},\n"
                f"fecha_nac={self.fecha_nacimiento!r},\n)")
    
    def __str__(self)-> str:
        """Representa al alumno de una manera legible para el usuario"""
        return (
                f"Id_curso:{self.id_curso}\n"
                f"Id_Alumno:{self.id_alumno}\n"
                f"-Alumno: {self.nombre} {self.apellido}\n"
                f"-DNI: {self.dni}\n"
                f"-Legajo: {self.legajo}\n"
                f"-Fecha Nacimiento: {self.fecha_nacimiento}\n"
                )
    def __lt__(self,other)-> bool:
        """
        Compara dos alumnos por su fecha de nacimieinto,
        el mas joven lo devuelve como menor
        """
        return self.fecha_nacimiento > other.fecha_nacimiento
    
    def __eq__(self, other: "Alumno")->bool:
        """
        Compara alumnos por su legajo
        Args:
            other (Alumno): Otro alumno con el que se compara la instancia actual.

        Returns:
            bool: True si ambos alumnos tienen el mismo legajo, False en caso contrario.
        """
        return self.legajo==other.legajo
    
    def __hash__(self)-> int:
        """
        Utiliza el legajo del alumno como hash,
        para estructuras como set, dicts
        """
        return hash(self.legajo)