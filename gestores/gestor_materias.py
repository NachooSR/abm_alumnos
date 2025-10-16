class GestorMaterias:
    def __init__(self):
        self.materias = []

    def agregar_materia(self,materia):
        self.materias.append(materia)

    def listar_materias_curso(self,id_curso):
        listado= [materia for materia in self.materias if materia.id_curso == id_curso]
        return listado