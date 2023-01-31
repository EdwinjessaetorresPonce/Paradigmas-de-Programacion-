from multiprocessing import Pool
import os
import random


def montecarlo(N:float) ->int:
    semilla:float = random.uniform(-1,1)
    random.seed(semilla)
    sentro:int = 0
    for i in range(N):
        x:float = random.uniform(-1,1)
        y:float = random.uniform(-1,1)
        if (x*x + y*y) < 1.0:
            dentro += 1
    return dentro

if __name__ == "__main__":
    n:int = 1.0e7
    cpus = os.cpu_cout()
    N: int = int(n/cpus)
    print("procesadores = ", cpus)
    arg = [N for i in range(cpu)]

    #El objeto grpo tiene matodo map para repetir tarea
    results = Pool(cpus).map(montecarlo,arg)
    print("Numero de tiros = ", cpus*N)
    print("Numero de aciertos ", results)
    print("Aproximacion de pi = ", 4*sum(results)/(cpus*N))

