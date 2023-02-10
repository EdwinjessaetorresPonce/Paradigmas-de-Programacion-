#=============================
# Clase computadora
#=============================
class Computadora:
    marca: str = None
    capacidad: int = 0
    ram: int = 0
    
    #==========================
    # Constructor
    #==========================
    def __init__(self, marca:str, capacidad:int, ram:int):
        print(f"Accedimiento al constructor da la pc: {marca}")
        self.marca = marca
        self.capacidad = capacidad
        self.ram = ram
    
    def imprimirInfoPC(self):
        print(f"Esta es la computadora marca: {self.marca} con almacenamiento de {self.capacidad}GB y memoria de {self.ram}GB")
        
    #==================
    # Destructor
    #==================
    def __del__(self):
        print(f"Se elimino la computadora: {self.marca}")

#=======================
#Objeto persona
#=======================
class Persona:
    nombres: str = None
    apellidos: str = None
    edad: int = None
    direccion: str = None
    computadora: Computadora = None
    
    #====================
    #Construccion de persona
    #====================
    def __init__(self, nombres:str, apellidos:str, edad:int, direccion:str, marca:str, capacidad:int, ram:int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.dereccion = direccion
        self.Computadora = Computadora(marca, capacidad, ram)
        print(f"---Accedimos al constructor de la persona: {nombres} {apellidos}")
        
    def imprimirInfo(self) -> None:
        print(f"---Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años de edad, vivo en {self.direccion}")
        self.Computadora.imprimirInfoPC()
    
    
    #==========================
    #Destructor
    #==========================
    def __del__(self):
        print(f"--- Eliminamos el objeto... {self.nombres} {self.apellidos}")
    
#======================================
# Funcion 1 es el  programa
#======================================
def funcion1():
    persona = Persona("Carlos", "Perez", 40,"Xochimilco", "Lenovo", 700, 8)
    print("\n")
    persona2 = Persona("Magdalena", "Carrillo", 35, "Jalapa", "IBM", 200, 4)
    print("\n")
    persona2.imprimirInfo()
    print("\n")

#=====================
#llamar a funcion1
#=====================
funcion1()
    



