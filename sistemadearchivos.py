from aplicacion.repositorio.repositoriodeusuario import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#=============================================
#implementa la interface RepositorioDeUsuarios
"""
"f"lo que sea {dato}" -> esto hace una relacion entre str y 
datos o funciones para que no tengas que estar cerrando comillas
cada que quieres llamar un dato o una funcion
"""
#=============================================
class SistemaDeArchivos(repositorioDeUsuario):
    __directorio: str
    
    def __init__(mi, directorio:str):
        mi.__directorio = directorio
        
    def abrir(mi) -> None:
        print(f"Abrir directorio: {mi.__directorio}")
    
    def guardar(mi, usuario:Usuario) -> None:
        xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
        print(f"Guardando usuario en el archivo :{mi.__directorio}/{usuario.getNombre()}")
        print(xml)
        
    def cerrar(mi) -> None:
        print("Cerrar el archivo")
        
