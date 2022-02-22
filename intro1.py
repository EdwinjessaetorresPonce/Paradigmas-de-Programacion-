''' ESTE ES UN SUPER COMENTARIO
    DE INICIO A NUESTRO RESUMEN
'''
#================================
#Operaciones basicas 
#================================
print(2+3)
print(2*3)
print(2/3)
print(2**100)
print(2**0.5)   #raiz cuadrada 
print(10%2)     #residuo de 10 entre 2
print(10%0.1)

#===============================
#Para saber el tipo de objeto se usa type
#==============================

t=0
print(type(t)) 
t=3.6
print(type(t))
t=True
print(type(t))

#=======================================
#Mensaje a pantalla
#======================================

print ("Este es un comando de python." "Este es otro enunciado", t)
print('id: '' 1')
print('first name :' 'steve')
print('last name: ' 'jobs')
print("vamos a sumar esto" + "con esto otro")

#===============================================
#Continuar una indtruccion en varios renglones
#===============================================

if 100 > 99 and\
        200 <= 300 and \
        True != False:
            print('Hello world')

#================================================
#Comandos diferentes en la misma liena 
#================================================

print("hola"); print("tu!!") #se considera mala practica 

#================================================
''' Usando parentesis redondos, cuadrados o llaves 
se pede escribir en varios renglones '''
#===============================================

list = [ 1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

print(list)

matriz = [[1,2,3,4], [5,6,7,8], [9,10,11,12] ]

print(matriz)

#===================================================
#Indentacion escrita para procesos dependientes de : (dos puntos)
#===================================================

if 10>5:
    print("diez es mayor que cinco")
    print("otra indentacion")

for i in list:
    print (i)
    print("ok")

if 10>5:
    print("verdadero")

if 10<20: 
    print("verdadero")
elif 5>3: # segundo condicional
    print("esto no se imprimira")
else:
    print("aqi nunca llega")
#=======================================================
#Funciones 
#=======================================================

def say_hello (name):
    print("hello ", name)
    print("welcome to python tutorials" )

say_hello("Edwin")


















