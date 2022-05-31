#=========================== 1:45
#Funcion pura x**2
#===========================

def alcuadrado(x):
    return x*x

#============================
#Funcion pura x**3
#============================

def alcubo(x):
    return x*x*x

#==========================
#Mapeo de una funcion pura 
#===========================
def mapeo(func,lista_numeros):
    resultado = []
    
    for i in lista_numeros:
        resultado.append(func(i))
    return resultado

cuadrados = mapeo (alcuadrado,[2.5,2,3.8,1.2,6.6,1j,7,8])
cubos =mapeo(alcubo,[1,2,3,4,5,6,7,8,9])
print(cuadrados)
print(cubos)

#==============================
#Funciones dentro de funciones
#===============================
def en_mayusculas(texto):
    return texto.upper()    #upper() transforma el texto en mayusculas

def en_minusculas(texto):
    return texto.lower()    #lower() cambia el texto a minusculas

def saludar(func):
    saludo = func("HolA, Que Tal??")
    print(saludo)

#=========================
#Con strings
#=========================
saludar(en_mayusculas)
saludar(en_minusculas)

#=======================================
# funciones abtractas dentro de funciones
# su resultado es otra funcion
#========================================
def divisor(x):
    def dividendo(y):
        return y/x
    return dividendo

#==========================================
# Primero generaremos la funcion y/2
#==========================================
division = divisor(2)

#===========================================
# la usaremos para calcular 3/2
#===========================================
print(division(3))


#================================================
# uso de la funcion map con una lista 
#=================================================

#==================================================
# Lista de ciudades y su temperatura 
#==================================================
temps = [("Berlin", 29), ("cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27), ("Nueva York", 28),("Londres", 22), ("Pekin",32),("Mexico Tenochtitlan", 23)]

C_a_F = lambda datos: (datos[0], (9/5)*datos[1] + 32)
print(list(map(C_a_F,temps)))





















