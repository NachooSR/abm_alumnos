from models import Alumno
from .gestor_cursos import GestorCursos
from .gestor_materias import GestorMaterias
from utils.decorators import log_action

class GestorAlumnos:
    
    def __init__(self,gestor_cursos,gestor_materias):
        self.gestor_cursos = gestor_cursos
        self.gestor_materias = gestor_materias
        self.listado_alumnos= []

    #region CRUD    
    @log_action("agregar alumno")
    def agregar_alumno(self, alumno):
        
        #Id del curso validado
        if not self.gestor_cursos.exist_curso(alumno.id_curso):
            raise ValueError("Curso inexistente")
        
        #Legajo unico
        if self.exist_legajo(alumno.legajo):
            raise ValueError("El legajo ya existe")
        
        #Validar que no exista ya cargado el dni
        if self.exist_dni(alumno):
            raise ValueError("El dni ya existe en el curso")
        
        self.listado_alumnos.append(alumno)

    def exist_legajo(self,legajo):
        return any(a.legajo == legajo for a in self.listado_alumnos)
    
    def exist_dni(self,alumno):
        return any(a.dni == alumno.dni for a in self.listar_alumnos_curso(alumno.id_curso))
    
    def listar_alumnos_curso(self,id_curso):
        lista_personalizada = [alumno for alumno in self.listado_alumnos if alumno.id_curso == id_curso]
        return lista_personalizada
    
    def mostrar_alumnos_curso(self,id_curso):
        curso = self.gestor_cursos.buscar_curso(id_curso)
        print(f"\nCurso: {curso.anio} {curso.nombre}")
        print(f"Profesor: {curso.profesor}\n")
        lista= self.listar_alumnos_curso(id_curso)
        for a in lista:
            print(a)

        
    def encontrar_alumno(self,legajo):
        if not self.exist_legajo(legajo):
            raise ValueError("Legajo doesnt exist")
        for a in self.listado_alumnos:
            if a.legajo == legajo:
                return a

    def mostrar_alumno(self,legajo):
        alumno = self.encontrar_alumno(legajo)
        print(f"\nNombre:{alumno.nombre} {alumno.apellido}")
        print(f"\nDNI:{alumno.dni}")
        print(f"\nFecha nacimiento:{alumno.fecha_nacimiento} ")
        print(f"\nId Curso:{alumno.id_curso}")

    def edit_alumno(self,leg_edit,**kwargs):
        for a in self.listado_alumnos:
          if a.legajo == leg_edit:
           for key,value in kwargs.items():
             if key== "legajo":
                raise ValueError("Legajo cannot be edited")
             setattr(a,key,value)
        print("Alumno editado correctamente")
    
    def eliminar_alumno(self,legajo):
        if not self.exist_legajo(legajo):
            print("Legajo dont exist")
        for a in self.listado_alumnos:
            if a.legajo== legajo:
                self.listado_alumnos.remove(a)
                print("Alumno eliminado correctamente")
                return
        print("Hubo un error")
    
    #endregion

    #Metodo auxiliares
    