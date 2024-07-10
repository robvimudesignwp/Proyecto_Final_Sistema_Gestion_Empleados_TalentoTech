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
  
## Creando la calse Jefe      
class Jefe(Empleado):
     def __init__(self, nombre, apellido, edad, salario, nro_identidad, fecha_vinculacion):
          super().__init__(nombre, apellido, edad, salario, nro_identidad, fecha_vinculacion)
          self.empleados_al_mando = []
     
     def insertar_empleado(self, empleado):
          for trabajador in self.empleados_al_mando:
               if trabajador == empleado:
                    print(f"Empleado {empleado.nombre_completo()} ya está al mando del Jefe {self.nombre_completo()}.\n")
                    return
          self.empleados_al_mando.append(empleado)
          print(f"Empleado {empleado.nombre_completo()} añadido bajo el cargodel Jefe {self.nombre_completo()}.\n")
          
     def suprimir_empleado(self, nro_identidad):
          for trabajador in self.empleados_al_mando:
               if trabajador == nro_identidad:
                    self.empleados_al_mando.remove(trabajador)
                    print(f"Empleado {trabajador.nombre_completo()} eliminado bajo el cargo del Jefe {self.nombre_completo()} (Carta de despido).\n")
                    return
               print(f"No se encontró ningún empleado con cédula {nro_identidad} bajo el cargo del Jefe {self.nombre_completo()}.\n")
               
     def obtener_empleados_al_mando(self):
          return [empleado.nombre_completo() for empleado in self.empleados_al_mando]
     
     def obtener_informacion_empleados(self):
          empleados_str = ",".join(self.obtener_empleados_al_mando()) or "Ninguno"
          return super().obtener_informacion_empleados() + f"\nEmpleados al mando: {empleados_str}\n"
     