#===========================
# mpirun -n 4 python3 tareas_mpi.py
#===========================
from mpi4py import MPI

#===========================
# Objeto de comunicadores
#===========================
comm = MPI.COMM_WORLD

#===========================
#cuantos somos en total
#===========================
size = comm.Get_size()

#==========
# Quien soy 
#==========
rank = comm.Get_rank()

#===================================
#si yo soy el proceso cero hago esto
#===================================
if rank == 0:
    print("Yo soy el proceso 0")

#==================================
#si yo soy el uno hago esto otro
#===================================
elif rank == 1:
    print("yo soy el proceso 1")

#===============================================
# si yo no soy ni el proceso 1 ni el 2 hago esto
#==============================================
else:
    print("yo no soy ninguno de los dos primeros procesos")

print("Reportandome soy el proceso ", str(rank), "de ", str(size))

