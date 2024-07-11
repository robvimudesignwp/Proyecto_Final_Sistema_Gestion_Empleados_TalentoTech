## Creando la clase Trabajador
class Trabajador:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
listadoEmpleados = []

def Mostrar():
   e = 0
   while(e < len(listadoEmpleados)):
       print(listadoEmpleados[e].nombre, " ", listadoEmpleados[e].apellido, " ", listadoEmpleados[e].edad)
       e += 1
       
c = 0
while(True):
    print("+-----------------------+")
    print("| 1. Agregar Empleado   |")
    print("+-----------------------+")
    print("| 2. Consultar Listado  |")
    print("+-----------------------+")
    print("| 3. Salir del Programa |")
    print("+-----------------------+")
    
    opcionMenu = int(input("Por favor dígite una opción del menú:"))
    if(opcionMenu == 1):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        trabajador_01 = Trabajador(nombre, apellido, edad)
        listadoEmpleados.append(trabajador_01)
        print("¡Empleado guardado de forma exitosa!")
    elif(opcionMenu == 2):
        Mostrar()
    elif(opcionMenu == 3):
        exit()
    else:
        print("Lo sentimos no es una opción válida, intentalo de nuevo")
