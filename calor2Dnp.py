import numpy as np
import matplotlib as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from numba import jit

#===============================
#numero deceldas
n = np.array([512,512])
#Tamaño del dominio menor que 1
L = np.array([1.0,1.0])
#Constante de difusion
k = 0.2
#pasos de tiempo
pasos = 1000

#===================================

#TAMAÑO DE CELDAS
dx = L/n
udx2 = 1.0/(dx*dx)
#PASO DE TIEMPO
dt = 0.25*(min(dx[0],dx[1])**2)/k
print("dt = ", dt)
#TOTAL DE CELDAS
nt = n[0]*n[1]
print("celdas = ", nt)
#LLENAR LAS SOLUCIONES CON CEROS
u = np.zeros(nt,dtype=np.float64)  #arreglo de lectura
un = np.zeros(nt, dtype=np.float64) #arreglo de escritura

@jit(nopython=True)
def evolucion(u,n,udx2,dt,i,k):
    jpl = i + n[0]
    jml = i - n[0]
    laplaciano = (u[i-1]-2.0*u[i]+u[i+1])*udx2[0] + (u[jml]-2.0*u[i]+u[jpl])*udx2[1]
    unueva = u[i] + dt*k*laplaciano
    return unueva

@jit(nopython=True)
def solucion(u,un,udx2,dt,i,k):
    if i == int(nt/2)+int(n[2]/2):
        unueva = 1.0
        un[i] = unueva

x,y = np.meshgrid(np.arange(0,L[0],dx[0]),np.arange(0,L[1],dx[1]))
ax = plt.axes(projection='3d')
start = time.time()
for t in range(1, pasos+1):
    solucion(u,un,udx2,dt,n,k)
    u = un
    if t%100==0: print("Iteracion = ",t)
end = time.time()
print("Tardo: ", end-start,"s")
up= np.reshape(u,(n[0],n[1]))
ax.plot_surface(x,y,up,cmap=cm.hsv)
plt.show()
#6:50






    




