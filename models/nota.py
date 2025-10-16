class Nota:
    def __init__(self,id_materia,id_alumno,cuatrimestre,valor):
        self.id_materia= id_materia
        self.id_alumno= id_alumno
        self.cuatrimestre= cuatrimestre
        self.valor = valor
    
    
    def __str__(self):
        return (
            f"Id_Materia:  {self.id_materia}\n"
            f"Id_Alumno:   {self.id_alumno}\n"
            f"Cuatrimestre:{self.cuatrimestre}\n"
            f"Valor:       {self.valor}\n"
        )