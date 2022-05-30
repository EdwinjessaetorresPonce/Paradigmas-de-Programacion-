#===============================
# Primer funcion 
#=================================
def saludo( ):
    #===================
    #documentacion rapida de la funcion 
    #====================
    """esta funcion saluda"""
    print('quiuboles, ¿como estas?')

#====================
#llamando a la funcion 
#=======================
saludo( )

#=========================
#se ejuta pero no se asigna
#========================
salida = saludo()

#======================================
#esto no funciona 
#======================================
print(salida)

#=====================================
#mostrar la documentacion 
#========================================

#help(saludo)

#=====================================
# Funcion argumento 
#======================================

def saludo2(nombre): 
    """Esta funcion te saluda or tu nombre""" 
    print("Que onda ese " + str(nombre) + " !!" )

saludo2("Edwin")
saludo2("jessae")



#=================================================
#para ahorrarle trabajo a python tenemos que espesificar 
#que clase de variables va admitir nuestra funcion 
#==================================================

def saludos (nombre:str):
    """esta funcion admite unicamente str"""
    print("Que onda ese", nombre, "!!!")

saludos("Edwin")

a= 123
print(type(a))
saludos(a)


#=====================================================
#funcion con muchos argumentos
#=======================================================

def saludos_multiples (nombre1, nombre2, nombre3):
    """Esta saluda a 3 personas al mismo tiempo"""
    print("hola", nombre1, ",", nombre2, "y", nombre3)

saludos_multiples("Edwin", "Jesseae", "Luis")

#=============================================
#funcion con cualquier numero de argumentos 
#=============================================

def muchos_saludos (*nombres):
      """esta fncion saluda a las personas que quieras """
      i = 0
      #-----------------
      #end= es para ponerlo de corrido
      #-------------------
      print("hola ", end= "")
      while len(nombres) > i :
          #ultimo nombre 
          if (i == len (nombres)-1):
              print(nombres[i])
          else:
              #cualquier otro nombre
              print (nombres [i] , end= ", ")
          i+=1

muchos_saludos("Bosco", "Angel", "Tamara", "Mili", "Edwin", "Yahir")

def greet(firstname, lastname):
    print('Hello' ,firstname, lastname)

#========================================
#Llamar a la funcion con argumentos en desorden
'''Esto se puede hacer especificando a que es igual cada
valor sin que sea en orden '''
#==========================================
greet(lastname='Torres', firstname='Edwin') #3:47



#====================================================
#Funcion con argumentos escondidos **
#====================================================

def greet(**person):
    #---------------------------
    #persona tiene caracteristicas firstname y lastname
    #---------------------------
    
    print('Hello', person['firstname'], person['lastname'])

greet(firstname= 'Edwin', lastname='Ponce')
greet(lastname='Acosta', firstname='Luis')
greet(lastname='Juan', firstname='Suarez', age='19')

#=====================================================
#Funcion con valores por defecto 
#=====================================================

def greet(name = 'Edwin'):
    print('Hola', name)

greet()

#========================================================
#Funcion con resultado
#========================================================

def suma(a,b):
    return a + b 

#=========================================================
''' Programacion funcional
se pueden funciones en funciones '''
#=========================================================
total = suma(5, suma(10, 20))
print(total)

#=========================================================
'''Calculo de lamda
nombre de la funcion = lambda variable : funcion '''
#=========================================================
x_al_cuadrado = lambda x : x * x
al = x_al_cuadrado
print(al)


#=======================================
#lambda de varias variables
#========================================
suma = lambda x1, x2, x3 : x1 + x2 + x3
print(suma (99, 98, 97))

sumas = lambda *x: x[0] + x[1] + x[2] + x[3]
print(sumas(100, 200, 300, 400))

#==============================================
''' Uso de una funcion anonima 
el argumento va afuera entre parentecis '''
#==============================================

print((lambda x: x*x)(6)) #funcion anonima

#==============================================
'''Funcion con variables global
EVITE EL EXASO '''
#==============================================
name = 'Edwin'

def greet():
    global name #para utilizar una variable global (que viene del bloque)
    name = 'Jessae'
    print('Hello', name)

greet()




























