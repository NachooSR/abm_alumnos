class Materia:
    def __init__(self,id_curso: int,id_materia: int,nombre: str):
        """
        Inicializa una instancia de Materia
        
        Args:
            id_curso(int): Curso al cual pertenece la materia
            id_materia(int): Identificador unico de materia
            nombre(str): Nombre de la materia
        """
        self.id_curso= id_curso
        self.id_materia= id_materia
        self.nombre= nombre        
    def __str__(self)-> str:
        """Representacion de la materia legible para el usuario"""
        return (
            f"Id_Materia: {self.id_materia}\n"
            f"Id_Curso:   {self.id_curso}\n"
            f"Materia:    {self.nombre}\n"
        )
    def __repr__(self)->str:
        """Representacion tecnica de la materia (debugging)"""
        return (f"{type(self).__name__}(\n"
                f"(id_curso={self.id_curso!r},\n"
                f"id_materia={self.id_materia!r},\n" 
                f"nombre={self.nombre!r},\n")