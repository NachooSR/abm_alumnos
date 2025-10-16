from models import Curso

class GestorCursos:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self,curso):
        if self.exist_curso(curso.id_curso):
            raise ValueError("Id Exist")
        self.cursos.append(curso)
     

    def exist_curso(self,id_curso):
       return self.buscar_curso(id_curso) is not None
    
    def buscar_curso(self,id_curso):
        for c in self.cursos:
            if c.id_curso == id_curso:
                return c
        return None        