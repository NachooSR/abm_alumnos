from models import Alumno,Curso,Materia,Nota
from gestores import GestorCursos,GestorAlumnos,GestorMaterias
from utils import *




if __name__ == "__main__":

    #region Inicializaciones
    
    #Gestores
    gestor_cursos = GestorCursos()
    gestor_materias= GestorMaterias()
    gestor_alumnos = GestorAlumnos(gestor_cursos, gestor_materias)
    

    #Cursos
    curso1 = Curso(1, 2024, "Prof. Gómez", "1° Año A")
    curso2 = Curso(2, 2024, "Prof. Martínez", "2° Año B")
    curso3 = Curso(3, 2025, "Prof. Ramírez", "3° Año A")

    gestor_cursos.agregar_curso(curso1)
    gestor_cursos.agregar_curso(curso2)
    gestor_cursos.agregar_curso(curso3)


    #Materias
    materias = [
    Materia(1, 101, "Matemática I"),
    Materia(1, 102, "Lengua y Literatura"),
    Materia(1, 103, "Historia"),
    Materia(2, 201, "Matemática II"),
    Materia(2, 202, "Física"),
    Materia(2, 203, "Química"),
    ]

    for materia in  materias:
        gestor_materias.agregar_materia(materia)

    #Alumnos
    alumnos = [
    Alumno(1,1, "A001", "Lucas", "Pérez", "40011222", "06/01/2003"),
    Alumno(2,1, "A002", "María", "López", "40022333", "10/07/2007"),
    Alumno(3,2, "A003", "Juan", "García", "39987654", "17/10/2005"),
    Alumno(4,2, "A004", "Sofía", "Rodríguez", "39845231", "10/05/2002"),
    Alumno(5,3, "A005", "Tomás", "Fernández", "39776544", "06/01/2002"),
    ]    

    for alumno in alumnos:
        gestor_alumnos.agregar_alumno(alumno)


    #gestor_alumnos.mostrar_alumnos_curso(1)
    #endregion
    
    condicion= True

   #"A001" --> Legajo para testear

    while condicion:
        menus.menu_inicial()
        option = int(input())
        match option:
            case 1:
                menus.menu_alumnos()
                option = int(input())
                match option:
                    case 1:
                        aux= interfaz.cargarAlumno()
                        gestor_alumnos.agregar_alumno(aux)
                        print(f">>>>Alumno ID:{aux.id_alumno} agregado correctamente")
                        # gestor_alumnos.mostrar_alumno(aux.legajo) el alumno se agrega
                    case 2:
                        legajo_buscar= input("Ingrese legajo a editar: ").strip()
                        exist_alumno= gestor_alumnos.exist_legajo(legajo_buscar)
                        if not exist_alumno:
                            print("Lo sentimos el alumno no existe")
                        else:
                            print("\n>>>>Este es su alumno")
                            gestor_alumnos.mostrar_alumno(legajo_buscar)
                            ok = int(input("Es correcto? 1-Si 0-No"))
                            if ok == 1: 
                                menus.menu_edit()
                                opcion_edit= int(input())
                                match opcion_edit:
                                    case 1:
                                        nombre_edit= input("Nuevo nombre: ")
                                        gestor_alumnos.edit_alumno(legajo_buscar,nombre= nombre_edit)
                                    case 2:
                                        apellido_edit= input("Nuevo apellido: ")
                                        gestor_alumnos.edit_alumno(legajo_buscar,apellido= apellido_edit)
                                    case 3:
                                        dni_nuevo = input("Dni: ")
                                        valido= interfaz.validar_dni(dni_nuevo)
                                        if valido:
                                            gestor_alumnos.edit_alumno(legajo_buscar,dni= dni_nuevo)
                                        else:
                                            print("Lo sentimos hubo un error")
                                    case 4:
                                        id_curso_nuevo= int(input("Id Curso: "))
                                        if not gestor_cursos.exist_curso(id_curso_nuevo):
                                            print("El curso ingresado no existe")
                                        else:
                                            gestor_alumnos.edit_alumno(legajo_buscar,id_curso=id_curso_nuevo)
                                print(">>>>>>>>>Alumno modificado")
                                gestor_alumnos.mostrar_alumno(legajo_buscar)
                            else:
                                pass 
                            
            case 2:
                print("ERROR 404")
            case 3:
                print("Gracias")
                condicion= False
            case _:
                print("Opcion invalida")
