import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from numba import jit
from numba import cuda
from numba import *

#===========================
#NUMERO DE CELDAS
n = np.array([512,512],dtype=np.int64)
#TAMAÑO DEL DOMINIO MENOR QUE UNO
L = np.array([1.0,1.0],dtype=np.float64)
#CONSTANTE DE DIFUCION
kd:float64 = 0.2
#PASO DE TIEMPO
pasos: int = 1000
#===============================

#TAMAÑO DE LAS CELDAS
dx = L/n
udx2 = 1.0/(dx*dx)
#PASO DE TIEMPO
dt = 0.25*(min(dx[0],dx[1])**2)/kd
#TOTAL DE CELDAS
nt = n[0]*n[1]
print("celdas : ", nt)

@jit
def evolucion(u,n_0,n_1,udx2_0,udx2_1,df,kd,i):
    jpl = i + n_0
    jml = i - n_0
    laplaciano = (u[i-1]-2.0*u[i]+u[i+1])*udx2_0 +(u[jml]-2.0*u[i]*u[jpl])*udx2_1
    unueva = u[i] + dt*kp*laplaciano
    return unueva

evolucion_gpu = cuda.jit(device=True)(evolucion)

@cuda.jit
def solucion_kernel(u_d,un_d,udx2_0,udx2_1,dt,n_0,n_1,kd):
    ii, jj = cuda.grid(2)
    i = ii + n_0*jj
    if i == int((m_0*n_1)/2)+int(n_0/2):
        unueva = 1.0
    un_d[i] = unueva

blockdim = (32,16) #HILOS POR BLOQUE
griddim = (int(n[0]/blockdim[0]),int(n[1]/blockdim[1])) #bloques en el dominio

#===============================
"""
PROGRAMA PRINCIPAL
"""
#===============================
start = time.time()
#LLENAR LA SOLUCION CON CEROS
u = np.zeros(nt,dtype=np.float64) #arreglo de lectura
un = np.zeros(nt,dtype=np.float64) #arreglo de escritura
#pasar arreglos al GPU
u_d = cuda.to_device(u)
un_d = cuda.to_device(un)
#INTEGRAR EN EL TIEMPO
for i in range(1,pasos+1):
    solucionkernel[griddim,blockdim](u_d,un_d,udx2[0],udx2[1],dt,n[0],n[1],kd)
    u_d = cuda.to_device(un_d)
    if t%100==0: print ("paso = ",t)
#PASAR ARREGLO AL CPU
end = time,time()
print("Tardo: ", end-start,"s")
#===================================

#------------------
#GRAFICAR EN 3D
#------------------
u = np.reshape(u,(n[0],n[1]))
x,y = np.mashgrid(np.arange(0,L[0],dx[0]),np.arange(0,L[1],dx[1]))
ax = plt.axes(projection='3d')
ax.plot_surface(x,y,u, cmap=cm.hsv)
plt.show()
 
