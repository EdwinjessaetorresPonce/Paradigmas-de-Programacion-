#===============================
#Recursividad y memoizacion
#===============================

#=================================
#1) INTENTO
#Herramientas para memoizacion
#=================================
from functools import lru_cache

def fibonacci_lento(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2:
        return fibonacci_lento(n-1)+fibonacci_lento(n-2)

#for i in range(1,36):
#    print(str(i) + ":" + str(fibonacci_lento(i)))


#===========================================================
#2) INTENTO
# Optimizacion 2: uso de conjuntos para guardar valores
#============================================================

#========================
#conjunto de fibinaccis
#========================
fibonaccis = {}
def fibonacci(n):
    
    '''
    # Revisa si ya existe y regresa el valor 
    '''
    if n in fibonaccis:
        return fibonaccis[n]
    
    if n==1:
        valor = 1
    elif n==2:
        valor = 1
    elif n > 2:
        valor = fibonacci(n-1) + fibonacci(n-2)
    
    
    #=============
    #Guardalo
    #=============
    fibonaccis[n] = valor
    return valor

#for i in range(1,10001):
#    print(str(i) + ":" + str(fibonacci(i)))


#========================================
''' Uso de decoradores para memoizacion
maxsiza: es cuando anteriores guarde '''
#=========================================
@lru_cache(maxsize = 3)
def nfibonacci(n):
    if type(n) != int:
        raise TypeError("n debe ser entero positivo")
    if n<1:
        raise ValueError("n debe ser entero positivo")
    
    if n==1:
        return 1
    
    elif n==2:
        return 1
    
    elif n>2:
        return nfibonacci(n-1) + nfibonacci(n-2)

for i in range(1,1001):
    print(" * " + str(i) + ":" + str(nfibonacci(i) ) )

#1:31
         






























