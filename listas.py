# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 09:29:19 2022

@author: HP_1
"""

#====================================================
#LISTAS []
#pueden ser de objetos diferentes
#====================================================
#lista vacia
lista1 = []
print(lista1)

#=======================================================
#agrega elementos listas 
#========================================================

lista1=[1, "Javier", 1.100000, "Edwin", "Bosco", True]
print(lista1)

#=========================================================
#hacer una lista con rangos
#range (i, j-1)
#=========================================================
nums = list (range(0,61))
print (nums)


#=========================================================
#incluir elementos a la lista append
#=========================================================

nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

#===========================================================
#quitar elementos de la lista
#============================================================
#nums.remove(61)
#print(nums)

#============================================
#eliminar el elemento i de la liata
#====================================================

del nums[63]
print (nums)

#===========================================================
#borrar lista
#========================================================
del nums

#================================
#Sumar Listas
#================================
L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(L1 + L2)

#==========================
#Llenado a mano
#==========================
potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])

#===============================
#Generar una tupla con lista
#===============================
potencial = tuple(potencial)
print(potencial[100])




































