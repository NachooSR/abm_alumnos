def menu_inicial():
    """Menu principal que se mostrara al usuario"""
    menu = """
----------------------
MENU PRINCIPAL
----------------------
1-Administrar alumnos 
2-Administrar notas
3-Salir
---------------------- 
"""
    print(menu)

def menu_alumnos():
    """Submenu para administrar alumnos"""
    
    menu = """
----------------------
MENU ALUMNOS
----------------------
1- Cargar Alumnos 
2- Editar Alumnos
3- Dar de baja Alumno
4- Mostrar alumno
5- Mostrar Curso
---------------------- 
"""
    print(menu)
    
def menu_notas():
    """Submenu para administrar notas"""
    
    menu = """
    ----------------------
        MENU NOTAS  
    ----------------------
    1-Administrar alumnos 
    2-Administrar notas
    ---------------------- 
    """
    print(menu)

def menu_edit():
    """Submenu para elegir que editar del alumno"""
    
    menu = """
    ----------------------
       Que desea editar  
    ----------------------
    1-Nombre
    2-Apellido
    3-DNI
    4-Fecha nacimiento
    5-Cambiar de curso
    ---------------------- 
    """
    print(menu)
