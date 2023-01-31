from multiprocessing import Process
import random
import os

N:int = 10 

def fenerador(N:float) -> None:
    semilla:float = random.uniform(-1,1)
    print("La semilla es: ", semilla)
    random.seed(semilla)
    random.seed(semilla)
    for i in range(N):
        x:float = random.uniform(-1,1)
        y:float = random.uniform(-1,1)
        print("x = ", x, "\t y = ", Y)

procesos = []
cpus = os.cpu_count()
print("Procesadores = ", cpus)
for i in range(cpus):
    procesos.append(Process(target=generador, args=(N,)))

