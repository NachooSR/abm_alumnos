class Materia:
    def __init__(self,id_curso,id_materia,nombre):
        self.id_curso= id_curso
        self.id_materia= id_materia
        self.nombre= nombre        
    def __str__(self):
        return (
            f"Id_Materia: {self.id_materia}\n"
            f"Id_Curso:   {self.id_curso}\n"
            f"Materia:    {self.nombre}\n"
        )
    def __repr__(self):
        return (f"{type(self).__name__}(\n"
                f"(id_curso={self.id_curso!r},\n"
                f"id_materia={self.id_materia!r},\n" 
                f"nombre={self.nombre!r},\n")