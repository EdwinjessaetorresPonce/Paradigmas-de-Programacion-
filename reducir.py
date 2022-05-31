#====================================
# Uso de reducciones (colapsar resultados)
#====================================

#=========================================
# Multiplicacion de todos los numeros en la lista
#============================================
from functools import reduce

bigdata = [2,3,5,7,11,13,17,19,23,29]

#=============================================
# Funcion x*y 
#=============================================
multiplicar = lambda x,y : x*y

print(reduce(multiplicar,bigdata))

#===============================================
""" 
Reduce la aplicacion de la funcion por partes a los resultados y
el siguiente elemento comenzando con los primeros elementos 
"""
#=================================================
