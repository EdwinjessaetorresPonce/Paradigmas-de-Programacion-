#=========================================
# del directorio aplicacion, el subdirectorio repositorio, 
# el archivo basededatos.py : traer el objeto Badededatos
#=========================================
from aplicacion.repositorio.basededatos import BaseDeDatos

#===============================================
# del directorio aplicacion, el subdirectorio repositorio,
# el archivo s3.py : trae el objeto s3 
#===============================================
from aplicacion.repositorio.s3 import s3

#===============================================
#del directorio aplicacion, el sudirectorio repositorio,
# el archivo s3.py : trae el objeto s3
#===============================================

from aplicacion.repositorio.s3 import S3

#==================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo sistemadearchivos.py: traer el objeto SistemaDeArchivos
#==================================================
from aplicacion.repositorio.sistemadearchivos import SistenmaDeArchivos

#======================================
#Del directorio aplicacion, el suddirectorio modelos,
# el archivo usuario.py : trae el objeto Usuario
#======================================
from aplicacion.modelos.usuario import Usuario 

#===========================================
#Del directorio aplicacion, el subdirectorio negocios,
#el archivo usuario.py : trae el objeto Usuario
#===========================================
from aplicacion.negocios.manejodeinscripciones.py import ManejoDeInscripciones

#===============================================
#Crea el objeto Usuario
#===============================================
usuario = Usuario("Roberto","Jimenez",18)

#===============================================
# Crea el objeto s3
#===============================================
repositorioS3 = S3("321321321","sdf34223","MiCubeta")

#===============================================
#Interface inscribirUsuario del objeto ManejoDeInscripciones
#===============================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#==================================================
#crear el objeto sistema de archivos
#==================================================
repositorioSisremaDeArchivos("/home/users")

#==================================================
#Interface inscribirusuario del objeto ManejoDeInscripciones
#==================================================
ManejoDeInscripciones.incribirUsuario(usuario,repositorioSistemaDeArchivos)

#==================================================
#Crear el objeto base de datos
#==================================================
repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

#==================================================
#interface inscribirUsuario del objeto ManejoDeInscripciones
#==================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")





























