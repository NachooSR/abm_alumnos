from models import Alumno
from gestores import GestorAlumnos

def cargarAlumno()-> Alumno:
    """
    Funcion encargada de cargar los datos
    de un alumno mediante la consola

    Returns:
        alumno(Alumno): Alumno con sus datos cargados
    """
    
    condicion = True 
    
    while condicion:
        print("Ingrese DNI: ")
        dni = str(input().strip())
        booleano =validar_dni(dni)
        if booleano:
            condicion = False
        else:
            print("Invalid Format DNI, Try Again")
    nombre=input("Nombre:").strip()
    apellido=input("Apellido:").strip()
    legajo=input("Legajo:").strip()
    fecha_nacimiento=input("Fecha de nacimiento (DD/MM/AAAA):").strip()
    id_curso= int(input("Id_curso:"))
    id_alumno= int(input("Id_alumno:"))

    alumno_aux= Alumno(id_alumno,id_curso,legajo,nombre,apellido,dni,fecha_nacimiento)
    return alumno_aux
    
    

def validar_dni(dni: str)->bool:
    """
    Valida el dni del alumno mediante 
    su longitud o formato

    Args:
        dni(str): dni de la persona/alumno
    
    Returns:
        bool: True si es un dni valido, False caso contrario
    """
    if not dni.isdigit() or len(dni)<7 or len(dni)>9 :
        return False
    return True