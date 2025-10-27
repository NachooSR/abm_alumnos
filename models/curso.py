'''
Reestructuracion de proyecto--> "db"
'''
class Curso:
    
    def __init__(self,id_curso: int, anio: int,profesor: str,nombre: str):
        """
        Inicializa una instancia del curso
        
        Args:
            id_curso(int): Identificador unico
            anio(int): Entero que representa el grado 
            profesor(str): Nombre del profesor a cargo
            nombre(str): Ordinal del curso
        """
        self.id_curso= id_curso
        self.anio= anio
        self.profesor= profesor
        self.nombre = nombre

    def __repr__(self)-> str:
        """Representacion tecnica del curso (debugging)"""
        return (f"{type(self).__name__}(\n"
                f"(id_curso={self.id_curso!r},\n"
                f"anio={self.anio!r},\n" 
                f"profesor={self.profesor!r},\n")
    
