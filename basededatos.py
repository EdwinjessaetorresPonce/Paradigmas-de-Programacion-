from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuaeios
from aplicacion.modelos.usuario import Usuario

#======================================================
# para llenar la interface hay que heredar la clase 
#======================================================
class BaseDeDatos(RepositorioDeUsuarios):
    __host: str
    __user: str
    _password: str
    
    def __init__(mi, host:str, user:str, password:str):
        mi.__host = host
        mi.__user = user
        mi.__password = password
        
    def abrir(mi) -> None:
        print(f"Abriendo la conexion a la base de datos: {mi.__host}:{mi.__user}@{mi.__password}")
        
    def guardar(mi, usuario:Usuario) ->None:
        userElements = {"nombre": usuario.getNombre(),
                        "apellido": usuario.getApellido(),
                        "edad": usuario.getEdad() }
        print(f"Guardando el usuario en la base de datos {usuario.getNombre()}\n")
        print(f"INSERTAR DATOS DEL USUARIO ('{userElements['nombre']}','{userElements['apellido']})")
        
    def cerrar(mi) -> None:
        print("cerrar la conexion")
        
