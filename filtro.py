#=============================
# Uso de filtros 
#=============================

#============================================
# Hacer una lista de los numeros por arriba  
#=============================================

#Modulo de estasdistica 
import statistics

bigdata  = [1.3, 2.7, 0.8, 4.1, -0.1]
promedio = statistics.mean(bigdata)
print(promedio)

#==============================================================
# Has una lista de elementos que cumplan la condicion x> promedio
# Filter (condiciones, datos)
#==============================================================
print(list(filter(lambda x:x>promedio, bigdata)))

#==============================
# Limpiar datos
#==============================
paises = ["", "Argentina", "", "Brasil", "", "Chile", "", "Mexico", "", "Colombia", "", "", "Cuba", "Venezuela"]

#================================
# Filtrar lo que no tiene nada
#================================

print(list(filter(None, paises)))
