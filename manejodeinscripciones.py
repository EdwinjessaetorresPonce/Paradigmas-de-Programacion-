from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#=======================================
# Clase stormanager
# NO TIENE VARIABLES 
#=======================================

class ManejoDeInscipciones:
    #==============================================
    '''
    Decorador staticmethod.
    El objetivo solo tieme la funcion iscribirUsuario
    ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    el objeto maneoDeinscriopciones es la interface interface intercambiable
    '''
    @staticmethod
    def inscribirUsuario(usuario:Usuario, repositorioDeUsuarios: RepositorioDeUsuarios )-> None:
        print("----> Guardando usuario . . . \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuario.guardar(usuario)
        repositorioDeUsuario.cerrar()
        

