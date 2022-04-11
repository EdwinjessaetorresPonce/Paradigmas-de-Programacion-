#============================================================
#PROGRAMACION ORIENTADA A OBJETOS
#============================================================

#--------------------------
#una clase para un objeto vacío 
#no esta tan vacio, necesita la palabra 
# pass = pasar
#-------------------------

class Objetovacio:
    pass

#------------------
nada = Objetovacio()
print (type (nada))

#------------------------------
#Clase llamada llanta
#------------------------------

class Llanta:
    #-----------------------------
    # Variable cuenta es de toda la clase
    #----------------------------
    cuenta = 0
    #----------------------------
    #funcion constructora de identidad
    #_init_ es una funcion reservada 
    #comienza con uno mismo: self
    #pero puede ser otro nombre (mi)
    #parametros de entrada = default 
    #----------------------------
    def __init__(mi, radio=50, ancho=30, presion=1.5):
        #variable de la estructura completa llanta 
        Llanta.cuenta += 1
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

#--------------------
#Objetos (instanciados)
#--------------------
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion =1.2)
llanta3 = Llanta() 
llanta4 = Llanta(40,30,1.6)

#------------------------------------
#Objetos que contienen otros objetos 
#------------------------------------
class Coche:
    def __init__(mi, ll1, ll2, ll3, ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print ("total de llantas: ", Llanta.cuenta)
print ("presion total de la llanta",llanta4.presion)
print("Radio de la llanta 4 = " , llanta4.radio)
print("Presion de la llanta 1 de mi coche = ", micoche.llanta1.presion)

#======================
#encapsulamiento
#======================

#============================
#uso de la funcion de python property para poner y obtener atributos 
#============================

class Estudiante :
    def __init__(mi):
        mi.nombre = ' '
    def ponerme_nombre (mi, nombre):
        mi.__nombre = nombre 
    def obtener_nombre (mi):
        print ('se llamo a obtener nombre' )
        return mi.__nombre
    nombre = property (obtener_nombre,ponerme_nombre)

#=====================================================000
# Crear objeto estudiante sin nombre
#=======================================================

estudiante = Estudiante()

#=========================================================
''' ponerle nombre usando la propiedad nombre y el método pinerme_nombre 
(sin tener que llamar explicitamente la fincion  ) '''
#=========================================================

estudiante.nombre = "Diego"

#================================================================
''' Obtener el nombre con el método obtener_nombre
__nombre esa una variable encapsulada (no visible desde fuera)
(sin tener que llamar explicitamente a la funcion obtener_nombre) '''
#===============================================================

print(estudiante.nombre)

#ESTO NO FUNCIONA 
#print(estudiante.__nombre)

#======================
#Herencia de clases
#=======================

class Cuadrilatero:
    def __init__ (mi, a, b, c, d):
        mi.lado1= a
        mi.lado2= b
        mi.lado3= c 
        mi.lado4= d

    def perimetro (mi):
        p = mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print ( 'perimetro = ' + str(p))
        return p
#======================================================
''' su hijo del rectangulo 
rectangulo es hijo de cuadrilatero
rectangulo (cuadrilatero) '''
#=====================================================
class rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        #=====================
        #contructor de su madre
        #=====================
        super() .__init__(a, b, a, b)

#===============================================
# su nieto cuadrado
# su hijo rectangulo
#===============================================

class cuadrado (rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area
    #def perimetro(self):
    #   p = 4.0*self.lado1
    #   print("parimetro =", p)
    #   return p
    
#============================================
#crear un cuadrado 
#=============================================
cuadrado1 = cuadrado(5)

#=================================================
# Llamar al método perimetro de su abuelo cuadrilatero
#==================================================

perimetro1 = cuadrado1.perimetro()

#=======================================================
#Llamar a su propio metodo area 
#=======================================================

area1 =cuadrado1.area()

print ('perimetro = ' + str(perimetro1 ))
print ('Area = ' + str (area1))
































