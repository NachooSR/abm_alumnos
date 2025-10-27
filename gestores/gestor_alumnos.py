from models import Alumno
from .gestor_cursos import GestorCursos
from .gestor_materias import GestorMaterias
from utils.decorators import log_action

class GestorAlumnos:
    """
    Clase encargada de gestionar los alumnos
    """
    def __init__(self,gestor_cursos:"GestorCursos" ,gestor_materias: "GestorMaterias"):
        """
        Inicializa una instancia de Gestor
        
        Args:
            gestor_cursos(GestorCursos): Gestor utilizado para gestionar los cursos de alumnos
            gestor_materias(GestorMaterias): Gestor utilizado para gestionar las materias de alumnos

        """
        self.gestor_cursos = gestor_cursos
        self.gestor_materias = gestor_materias
        self.listado_alumnos= []

    #region CRUD    
    @log_action("agregar alumno")
    def agregar_alumno(self, alumno: "Alumno")-> None:
        """
        Agrega un nuevo alumno al sistema validando las condiciones requeriidas

        Args:
            alumno(Alumno): Alumno ya cargado con sus datos

        Raises:
            ValueError: Si el curso no existe
            ValueError: Si el legajo ya esta en uso
            ValueError: Si el dni ya existe en el curso
        
        """
    
        if not self.gestor_cursos.exist_curso(alumno.id_curso):
            raise ValueError("Curso inexistente")
        
        
        if self.exist_legajo(alumno.legajo):
            raise ValueError("El legajo ya existe")
        
        
        if self.exist_dni(alumno):
            raise ValueError("El dni ya existe en el curso")
        
        self.listado_alumnos.append(alumno)

    def exist_legajo(self,legajo: str)-> bool:
        """
        Verifica si hay algun alumno con el legajo enviado
        
        Args:
            legajo(str): identificador interno del alumno

        Returns:
            bool: True si existe, False caso contrario

        """
        return any(a.legajo == legajo for a in self.listado_alumnos)
    
    def exist_dni(self,alumno: "Alumno")-> bool:
        """
        Verifica si ya existe un alumno con el dni
        dado en el mismo curso
        
        Args:
            alumno(Alumno): Objeto de tipo Alumno (se utiliza su id_curso y su dni)

        Returns:
            bool: True si existe el dni, False caso contrario
        """
        return any(a.dni == alumno.dni for a in self.listar_alumnos_curso(alumno.id_curso))
    
    def listar_alumnos_curso(self,id_curso: int)-> list[Alumno]:
        """
        Lista a los alumnos del curso enviado
        Args:
            id_curso(int): Identificador del curso a listar
        
        Returns:
            list[Alumno]: Lista de alumnos del curso indicado

        """
        lista_personalizada = [alumno for alumno in self.listado_alumnos if alumno.id_curso == id_curso]
        return lista_personalizada
    
    def mostrar_alumnos_curso(self,id_curso: int)-> None:
        """
        Muestra a los alumnos del curso enviado
        
        Args:
            id_curso(int): Identificador del curso a mostrar
        """
        curso = self.gestor_cursos.buscar_curso(id_curso)
        print(f"\nCurso: {curso.anio} {curso.nombre}")
        print(f"Profesor: {curso.profesor}\n")
        lista= self.listar_alumnos_curso(id_curso)
        for a in lista:
            print(a)

        
    def encontrar_alumno(self,legajo: str)-> None|Alumno:
        """
        Busca un alumno por su legajo

        Args:
            legajo(str): Identificador interno del alumno
        
        Raises:
            ValueError: Si el legajo no existe
        
        Returns:
            alumno(Alumno): Alumno correspondiente al legajo
        """
        if not self.exist_legajo(legajo):
            raise ValueError("Legajo doesnt exist")
        for a in self.listado_alumnos:
            if a.legajo == legajo:
                return a

    def mostrar_alumno(self,legajo: str)-> None:
        """
        Muestra un unico alumno por consola

        Args:
            legajo(str): Identificador interno del alumno
        """
        alumno = self.encontrar_alumno(legajo)
        print(f"\nNombre:{alumno.nombre} {alumno.apellido}")
        print(f"\nDNI:{alumno.dni}")
        print(f"\nFecha nacimiento:{alumno.fecha_nacimiento} ")
        print(f"\nId Curso:{alumno.id_curso}")

    @log_action("editar alumno")
    def edit_alumno(self,leg_edit: str,**kwargs: str|int)-> None:
        """
        Edita un alumno indicado por legajo
        
        Args:
            leg_edit(str): Legajo del alumno a editar
            **kwargs: Campos a modificar (nombre,apellido,curso,fecha_nacimiento,dni)
        
        Raises:
            ValueError: En caso de que se intente modificar el legajo
        """
        for a in self.listado_alumnos:
          if a.legajo == leg_edit:
           for key,value in kwargs.items():
             if key== "legajo":
                raise ValueError("Legajo cannot be edited")
             setattr(a,key,value)
        print("Alumno editado correctamente")
    
    @log_action("eliminar alumno")
    def eliminar_alumno(self,legajo: str)-> None:
        """
        Da de baja en el sistema a un alumno 
        indicado por legajo

        Args:
            legajo(str): Legajo del alumno
        
        Raises:
            ValueError: El legajo no existe
        """
        if not self.exist_legajo(legajo):
            print("Legajo dont exist")
        for a in self.listado_alumnos:
            if a.legajo== legajo:
                self.listado_alumnos.remove(a)
                print("Alumno eliminado correctamente")
                return
        print("Hubo un error")