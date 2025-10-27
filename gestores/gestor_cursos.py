from models import Curso

class GestorCursos:
    def __init__(self):
        """
        Inicializa una instancia de gestor de 
        cursos con una lista de cursos vacia
        """
        self.cursos = []

    def agregar_curso(self,curso: "Curso")-> None:
        """
        Agrega cursos al gestor

        Args:
            curso(Curso): Recibe un curso previamente cargado
        
        Raises:
            ValueError: El id del curso no existe
        """
        if self.exist_curso(curso.id_curso):
            raise ValueError("Id Exist")
        self.cursos.append(curso)
     

    def exist_curso(self,id_curso: int)-> bool:
       """
       Verifica la existencia de un curso indicado por id

       Args:
            id_curso(int): Identificador del curso 

       Returns:
            bool: True si existe el curso, False caso contrario
       """
       return self.buscar_curso(id_curso) is not None
    
    def buscar_curso(self,id_curso: int)-> Curso|None:
        """
        Busca un curso indicado por id

        Args:
            id_curso(int): Identificador del curso a buscar
        
        Returns:
            curso(Curso): En caso de coincidencia devuelve el curso
        
        """
        for c in self.cursos:
            if c.id_curso == id_curso:
                return c
        return None        