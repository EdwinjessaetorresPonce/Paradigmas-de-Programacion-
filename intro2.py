#============================================
#input permite obtener datos del usuario e promter
#=============================================
nombre= input("dame tu nombre : ")
print ("hola como estas ? ", nombre)

#============================================
#los enteros son de precision limitada
#===========================================

y= 5000000000000000000000000000000000000000
print(y)

#==============================================
#se pueden delimitar los numeros con "_"
#==============================================

y= 500_000
print(y)

#================================================
#La funcion int() convierte strings y floats a enteros
#===================================================

numero = int(input("dame tu edad : "))
print (type(numero))
print ("te ves mas joven de " + str(numero))

#==================================================
#Notacion cientifica de flotantes utiliza E o e
#===================================================

x = 1.2e-09
print(x)

#===============================================
#La funcion float() convierte string y enteros a floats
#=================================================

y= float ("2.14")
print(y)
print (type(y))

#===================================================
""" Los ckomplejos se escribrn con la raiz de -1
y en la computadoara su utiliza "nj" "n"= numero
si pones la "j" sola la toma coma variable """
#====================================================

z = 1+5j
print(z)

"""
~ suma +
~ multiplicacion *
~ divicion /
~ exponente **
~ funcion piso //
~ Funciones para transformar numeros int() float() complex
~ Operaciones ads() round(redondea,n despues del puento) pow()
"""
print (round(3.141624780917,4))

#===============================================
#string en varias lineas
#===============================================

parrafo = """ en el bosque de la chinita
    la chinita se perdio """
print (parrafo)

#================================================
# funcion len() te da el tamaño de la string
#=================================================
n= len (parrafo)
print (n)


#==============================================
""" las palabras en un string ocupan lugares como en un arreglo
tambien de atras para adelante comenzando en -1 el ultimo, y el
primero siendo 0 """
#=================================================
palabra = "wachiturro"
print (palabra [-1])
print (palabra [9])
print (palabra)






























