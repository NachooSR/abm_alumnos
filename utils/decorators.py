import datetime
from typing import Callable,Any

def log_action(accion_realizar: str)-> Callable:
    """
    Decorador que registra en un archivo de log el resultado de una operacion 
    (exitosa o con error) ejecutada en un metodo.

    Args:
        accion_realizar (str): Descripcion de la accion a registrar( 
        agregar, eliminar o editar alumno).

    Returns:
        function: Decorador que envuelve la funcion original para registrar su ejecucion.
    """
    
    def decorador(func):
        
        def wrapper(*args: Any,**kwargs: Any):
            
            message =''
            info_extra=''
            operacion= accion_realizar.capitalize()


            date_now= datetime.datetime.now()
            date_currently= date_now.strftime("%d/%m/%Y - %H:%M:%S")
            
            if accion_realizar == "agregar alumno":
                #El parametro [0] seria self (la clase)

                alumno_aux= args[1]
                info_extra= f"Legajo:{alumno_aux.legajo}"
            
            else:
                legajo = args[1]
                info_extra= f"Legajo:{legajo}"

            try:
                resultado = func(*args,**kwargs)
                message=f"[{date_currently}] Operacion ({operacion}) Exitosa-> {info_extra}\n"
            except ValueError as e:
                message=f"[{date_currently}] Operacion ({operacion}) Erronea-> {e}\n"
                resultado = None
                raise
            finally:
                with open ("data/logs.txt","a") as file:
                    file.write(message)
                return resultado
        return wrapper
    return decorador
