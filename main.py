from models import Alumno,Curso,Materia,Nota
from gestores import GestorCursos,GestorAlumnos,GestorMaterias
from utils import menus,decorators,interfaz
import json



if __name__ == "__main__":

    #region Inicializaciones
    
    #Gestores
    gestor_cursos = GestorCursos()
    gestor_materias= GestorMaterias()
    gestor_alumnos = GestorAlumnos(gestor_cursos, gestor_materias)
    

    lista_alumnos= []
    # try:
    #     with open("./data/alumnos.json") as file:
    #         payload= json.load(file)
    #         for alumno in payload:
    #             aux= Alumno(**alumno)
    #             lista_alumnos.append(aux)
    # except BaseException as e:
    #     print(f"Peto chaval  {e}")
    
    # for alumno in lista_alumnos:
    #     gestor_alumnos.agregar_alumno(alumno)

    # print(lista_alumnos)

    # gestor_cursos.agregar_curso(curso1)
    # gestor_cursos.agregar_curso(curso2)
    # gestor_cursos.agregar_curso(curso3)


    # for materia in  materias:
    #     gestor_materias.agregar_materia(materia)    

    # for alumno in alumnos:
    #     gestor_alumnos.agregar_alumno(alumno)


    #endregion
    
    # condicion= True
    # while condicion:
    #     menus.menu_inicial()
    #     option = int(input())
    #     match option:
    #         case 1:
    #             menus.menu_alumnos()
    #             option = int(input())
    #             match option:
    #                 case 1:
    #                     aux= interfaz.cargarAlumno()
                        
    #                     try:
    #                         gestor_alumnos.agregar_alumno(aux)
    #                         print(">>>Alumno agregado correctamente\n")
    #                     except ValueError as e:
    #                         print(e)
    #                 case 2:
    #                     legajo_buscar= input("Ingrese legajo a editar: ").strip()
    #                     exist_alumno= gestor_alumnos.exist_legajo(legajo_buscar)
    #                     if not exist_alumno:
    #                         print("Lo sentimos el alumno no existe")
    #                     else:
    #                         print("\n>>>>Este es su alumno")
    #                         exist = gestor_alumnos.exist_legajo(legajo_buscar)
    #                         if exist_alumno:
    #                             gestor_alumnos.mostrar_alumno(legajo_buscar)
    #                             ok = int(input("Es correcto? 1-Si 0-No:"))
    #                             if ok == 1: 
    #                                 menus.menu_edit()
    #                                 opcion_edit= int(input())
    #                                 match opcion_edit:
    #                                     case 1:
    #                                         nombre_edit= input("Nuevo nombre: ")
    #                                         gestor_alumnos.edit_alumno(legajo_buscar,nombre= nombre_edit)
    #                                     case 2:
    #                                         apellido_edit= input("Nuevo apellido: ")
    #                                         gestor_alumnos.edit_alumno(legajo_buscar,apellido= apellido_edit)
    #                                     case 3:
    #                                         dni_nuevo = input("Dni: ")
    #                                         valido= interfaz.validar_dni(dni_nuevo)
    #                                         if valido:
    #                                             gestor_alumnos.edit_alumno(legajo_buscar,dni= dni_nuevo)
    #                                         else:
    #                                             print("Lo sentimos hubo un error")
    #                                     case 4:
    #                                         fecha_nacimiento_edit= str(input("Fecha (DD/MM/AAAA):"))
    #                                         gestor_alumnos.edit_alumno(legajo_buscar,fecha_nacimiento= fecha_nacimiento_edit)
    #                                     case 5:
    #                                         id_curso_nuevo= int(input("Id Curso: "))
    #                                         if not gestor_cursos.exist_curso(id_curso_nuevo):
    #                                             print("El curso ingresado no existe")
    #                                         else:
    #                                             gestor_alumnos.edit_alumno(legajo_buscar,id_curso=id_curso_nuevo)
    #                                 print(">>>>>>>>>Alumno modificado")
    #                                 gestor_alumnos.mostrar_alumno(legajo_buscar)
    #                             else:
    #                                 print("Lo sentimos el legajo ingresado no existe")
    #                 case 3:
    #                     legajo_buscar= input("Ingrese legajo a dar de baja: ")
    #                     exist = gestor_alumnos.exist_legajo(legajo_buscar)
    #                     if not exist:
    #                         print("Legajo inexistente")
    #                     else:
    #                         gestor_alumnos.mostrar_alumno(legajo_buscar)
    #                         ok = int(input("Es correcto? 1-Si 0-No:"))
    #                         if ok == 1:
    #                             gestor_alumnos.eliminar_alumno(legajo_buscar)  
    #                             print(">>>>>>Alumno dado de baja")
    #                 case 4:
    #                     legajo_buscar=input("Legajo:")
    #                     exist = gestor_alumnos.exist_legajo(legajo_buscar)
    #                     if not exist:
    #                         print("Legajo inexistente")
    #                     else:
    #                         print(">>>>>>>>>>>>>>>")
    #                         gestor_alumnos.mostrar_alumno(legajo_buscar)
    #                         print(">>Enter to continue")
    #                 case 5:
    #                     id_curso=int(input("ID Curso:"))
    #                     exist = gestor_cursos.exist_curso(id_curso)
    #                     if not exist:
    #                         print("Curso inexistente")
    #                     else:
    #                         print(">>>>>>>>>>>>>>>")
    #                         gestor_alumnos.mostrar_alumnos_curso(id_curso)
    #         case 2:
    #             print("ERROR 404")
    #         case 3:
    #             print("Gracias")
    #             condicion= False
    #         case _:
    #             print("Opcion invalida")


'''
1) Cargar alumnos del json al gestor 


'''