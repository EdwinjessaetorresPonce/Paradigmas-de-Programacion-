from aplicacion.repositorio.repositoriodeusuarios import RepositorionDEUsuarios
from aplicacion.modelos.usuario import Usuario

#===========================================
# S3 es el hijo de RepositorioDeUsuarios
#===========================================
class S3(RepositorioDeUsuarios):
    __clienteId: str
    __secretKey: str
    __bucket: str
    
    def __init__(mi, clientId: str, secretKey: str, bucket: str):
        mi.__clientId = clienteId
        mi.__secretKey = secretKey
        mi.bucket = bucket
    
    def abrir(mi) -> None:
        print(f"Estableciendo conexion a AWS S3 {mi.__clientId}:{mi.__secretKey}")
        
    def guardar(mi, usuario:Usuario) -> None:
        userData = {"nombre": usuario.getNombre(),
                        "apellido": usuario.getApellido(),
                        "edad": usuario.getEdad()}
        print(f"Guardando usuario de la bandeja:{mi.__bucket}: {userData}")
    
    def cerrar(mi) -> None:
        print("cerrando conexion AWS")
        
        
