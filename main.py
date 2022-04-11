from aplicacion.banco.cliente_bancario import ClienteBancario

#============================================================
''' try: intentar (correr las instrucciones)
except: atrapar el error en una variable e
e: se puede convertir a string '''
#=============================================================

#========================================================
#Error por sacar mas dinero del que tiene
#========================================================

try:
    cliente = ClienteBancario("Jaime Andrade", "Hernandez Sánchez", 28, 0.0)
    cliente.guardarDinero(300)
    print (cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())
    
#=========================================================
#Exeption es el objeto más general de error
#=========================================================
except Exception as e:
    print("Error: " + str(e))

#=======================================================
#Error por usar un atributo privado
#=======================================================
try:
    print(cliente.__nombres)
except Exception as ex:
    print ("Error: " + str(ex))

#============================================
#Forma correcta
#============================================
print(cliente.nombres)






