from models.materia import *
class GestorMaterias:
    def __init__(self):
        """
        Inicializa una instancia de gestor de materias
        con una lista vacia de materias 
        """
        self.materias = []

    def agregar_materia(self,materia: "Materia")->None:
        """
        Agrega materias al gestor

        Args:
            materia(Materia): Materia previamente cargada
        """
        self.materias.append(materia)

    def listar_materias_curso(self,id_curso:int)-> list[Materia]:
        """
        Lista las materias de un curso indicado
        
        Args:
            id_curso(int): Identificador del curso

        Returns:
            list(Materia): Listado de las materias del curso
        """
        listado= [materia for materia in self.materias if materia.id_curso == id_curso]
        return listado
    