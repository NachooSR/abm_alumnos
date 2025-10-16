'''
Reestructuracion de proyecto--> "db"
'''
class Curso:
    
    def __init__(self,id_curso, anio,profesor,nombre):
        self.id_curso= id_curso
        self.anio= anio
        self.profesor= profesor
        self.nombre = nombre

    def __repr__(self):
        return (f"{type(self).__name__}(\n"
                f"(id_curso={self.id_curso!r},\n"
                f"anio={self.anio!r},\n" 
                f"profesor={self.profesor!r},\n")
    
