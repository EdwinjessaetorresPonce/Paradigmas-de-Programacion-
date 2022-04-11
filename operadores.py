#==========================================================
# Conjunto en python
#==========================================================

even_nums = {2, 4, 6, 8, 10}

print(even_nums)

#El booleano no es un conjunto 

emp ={1, "Edwin", 10.5, True}
print (emp)

nums ={ 1, 2, 3, 4, 5, 5, 6, 6, 6}
print (nums)

#=============================================================
#convertir secuencia a conjunto
#no lo genera en orden 
#===============================================================

s = set ("helloOLEH")
print (s)
s = set ((1, 2, 3, 4, 5)) # tupla a conjunto 
print (s)

#===============================================================
# De dicionario a conjunto : conjunto de llaves
#=============================================================

d = {1:"one", 2:"two"}
print(d)

s = set(d)
print(s) 

#agregar un elemento al conjunto
s.add (7)
print(s)

s.update (nums)
print(nums)

s.remove (2)
print(s)

s.update (nums)
print(nums)

s.remove (2)
print(s)

#----------------------------------------
#OPERACIONES DE CONJUNTOS
s1={1,2,3,4,5,6,7,8,9,10}
s2={2,4,6,8,10,12}

print(s1)
print(s2)

#Union (|)
su= s1|s2 
print(su)

#interseccion (&)
si= s1&s2
print(si)

#diferencia de conjuntos (-)
sr = s1-s2
print(sr)

#direncia simetrica (^)

ss= s1^s2
print(ss)

#========================================================
#DICCIONARIOS
# llave : valor
#=========================================================

capitals = {"USA": "WASHINTONG D.C." , "FRANCE" : "PARIS", "INDIA": "NEW DELHI"}
print(capitals)

#-------------------------
#Diccionario vacio
h = { }
print(h)

#-------------------------
# llave entera : valor string 

numsNames= {1 : "one", 2 : "two", 3 : "three"}
print (numsNames)

#Llave real, valor string
decNames= {1.5 : "one and half", 2.5: "two and half", 3.5 : "three and half "}
print(decNames)

#llave tupla, valor string
items={"colors":("blue","red","orage","yellow"), "refrigerator": ("LG", "samsung", "whirlpool")}
#print(items)
print(items["colors"])
#print(items["refrigerator"])
#print( items["refrigerator"] + items["colors"])

#llave string, valor int 
romanNums= {"I":1, "II":2, "III":3, "IV":4, "V":5}
#print(romanNums)
#print(str(items["colors"]) + str(romanNums["V"]))

#solo puedes llamar a las llaves y ellas traen a los valores
#hay diferentes formas de imprimir una llave pero es el mismo
#resultado
print(romanNums.get ("III"))
print(romanNums["III"])

#imprime uno por uno el valor de la llave y el valor
for k in capitals:
    print("Llave = " + str(k) + ", valor = " + str(capitals[k]))
    
#agregar datos en un diccionario 
capitals["MEXICO"] = "CDMX"
print(capitals)

#eliminar un elemento de la lista
del capitals ["USA"]
print (capitals)

#borrar todo el diccionario 
del capitals
#print (capitals)

#teda el valor de todas las llaves de la biblioteca
print(romanNums.keys())

#da el valor de to dos los valores de la biblioteca
print(romanNums.values())

#comprovar si una llave esta en una biblioteca
print("I" in romanNums)
print("XX" in romanNums)






























