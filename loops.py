#==============================================
#Condicionales
#=================================================
precio=51
#===========
#si esto.....
#============
if precio < 50:
    print("El precio es menor a 50")
#------------
#si no ... si esto otro...
#------------
elif precio > 50:
    print("el precio es mayor que 50")
#---------------
#si nada de lo anterior ...
#---------------
else:
    print("el precio 50")

precio = 50
cantidad = 5
total= precio*cantidad

#======================================
# condicionales anidados 
#=====================================

if total > 100:
    if total > 500:
        print("total es mayor a 500")
    else :
        if total < 500 and total > 400:
            print("total es menor que 500 pero maayor que 400")
        elif total < 500 and total > 300:
            print("total entre 300 y 500")
        else :
            print("total entre 100 y 300")

#=======================================
#condicional de igualdad ==
#========================================

elif total == 100: 
    print ("total es 100")
else :
    print("total menor que 100")

#================================================
#bucle while
#===================================================
num = 0
while num < 5: 
    num = num + 1 
    print ("num = ", num )

num = 0
while num<5:
    num += 1
    print ("num  = ", num)
    if num == 3:
        break

num = 0 
while num < 5 : 
    num += 1 
    if num > 3: 
        continue        #evitar lo siguiente, continuar con las iteracione
    print("num = ", num)

#===================================
#bucle sobre lista 
#===================================
nums = [10, 20, 30, 40]
for i in nums :
    print (i)

#=======================================
#bucle sobre un string
#======================================

for char in "hello" :
    print (char)

#=============================================================
#bucle sobre un diccionario 
# items = elementos
#================================================================

numNames =  { 1:'one', 2:'two', 3: 'three' }
for pair in numNames.items():
    print (pair)

#==================================================================
#bucle sobre diccionarios 
# key = llave 
# value = valor 
#======================================================================

for k, v in numNames.items():
    print("key = "+ str(k) + " , value =", str(v))




















