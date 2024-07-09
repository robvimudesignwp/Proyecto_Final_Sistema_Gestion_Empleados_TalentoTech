from datetime import datetime
## Creando la clase Empleado
class Empleado:
   def __init__(self, nombre, apellido, edad, salario, nro_identidad, fecha_vinculacion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__salario = salario
        self.__nro_identidad = nro_identidad
        self.__fecha_vinculacion = datetime.strptime(fecha_vinculacion, '%Y-%m-%d')
    
   def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"
    
    
   def get_sueldo(self):
       return f"Empleado: {self.nombre_completo}, Cédula: {self.__nro_identidad}, Salario: {self.__salario}\n"
   
   def get_datos_empleado(self):
       return (f"Nombre: {self.nombre_completo()}, Edad: {self.__edad}, Salario: {self.__salario}"
               f"Cédula: {self.__nro_identidad}, Fecha Vinculación: {self.__fecha_vinculacion.strftime('%Y-%m-%d')}\n")
       