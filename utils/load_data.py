import gestores
import  models
import json
 

def initial_load():
       
    lista_cursos=[]
    lista_materias=[]
    lista_alumnos= []

    try:
            with open("./data/cursos.json") as file:
                data_cursos= json.load(file)
                for curso in data_cursos:
                    curso_aux=models.Curso(**curso)
                    lista_cursos.append(curso_aux)
    except BaseException as e:
            print(f"Error:{e}")

    try:
            with open("./data/materias.json") as file:
                data_materias= json.load(file)
                for materia in data_materias:
                    materia_aux=models.Materia(**materia)
                    lista_materias.append(materia_aux)
    except BaseException as e:
            print(f"Error:{e}")

    try:
            with open("./data/alumnos.json") as file:
                data= json.load(file)
                for alumno in data:
                    aux= models.Alumno(**alumno)
                    lista_alumnos.append(aux)
    except BaseException as e:
            print(f"Error:{e}")
    
    return lista_alumnos,lista_cursos,lista_materias