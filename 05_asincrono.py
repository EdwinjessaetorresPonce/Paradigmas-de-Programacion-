import multiprocessing as mp
import numpy as np
import time

def my_function(i, param1, param2, param3):
    #calcular un polinomio
    result = param1**2 + param2 + param2
    #se hace tonta 2 segundos
    time.sleep(2)
    return(i,result)
def get_result(result):
    #se inscriben en la lista global
    #(mal estilo de programacion)
    global results
    results.append(result)

#=======================
#PROGRAMA PRINCIPAL
# ======================
if __name__ == "__main__":
    #Matriz  de 10x3 numeros al azar
    params = np.random((10,3))*100.0
    results  = []  #Lista : se encierran con corchetes [] y pueden al macenar elementos de diferentes datos y pueden al terarce 
    ts = time.time()
    
    #Un grupo de procesos (pool)
    pool = mp.Pool(mp.cpu_count())
    
    #loop de primera dimension del arreglo
    for i in range (0, params.shape[0]):
        #Corre asincronicamente my function con argumentos args y cuando termine corre get_results
        pool.apply_async(my_function, args = (i, params[i,0], params[i,1], params[i, 1], params[i,2]), callback=get_results)
        
        #Cerrar el grupo
        pool.close()
        #Esperar que termine el grupo
        pool.join()
        print("tiempo en paralelo = ", time.time()-ts)
        print(results)

    

