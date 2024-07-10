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
    
    
   def obtener_sueldo(self):
       return f"Empleado: {self.nombre_completo}, Cédula: {self.__nro_identidad}, Salario: {self.__salario}\n"
   
   def obtener_datos_empleado(self):
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
     
## Creando la clase Area

class Area:
     def __init__(self, nombre, descripcion):
          self.__nombre = nombre
          self.__descripcion = descripcion
          self.empleados = []
          self.jefe_area = None
          
     def insertar_empleado(self, empleado):
          for trabajador in self.empleados:
               if trabajador == empleado:
                    print(f"Empleado {empleado.nombre_completo()} ya está agregado en el área {self.__nombre}.\n")
                    return
               self.empleados.append(empleado)
               print(f"Empleado {empleado.nombre_completo()} insertado en el área {self.__nombre}.\n")
               
     def suprimir_empleado(self, nro_identidad):
          for trabajador in self.empleados:
               if trabajador == nro_identidad:
                    self.empleados.remove(trabajador)
                    print(f"Empleado {trabajador.nombre_completo()} eliminado del área {self.__nombre}.\n")
                    return
               print(f"No se encontró ningún empleado identificado con cédula {nro_identidad} en el área {self.__nombre}.\n")
               
     def designar_jefe(self, jefe):
          if isinstance(jefe, Jefe):
               self.jefe_area = jefe 
               print(f"Jefe {jefe.nombre_completo()} asignado al área {self.__nombre}.\n")
          
     def obtener_jefe_area(self):
          return self.jefe_area.nombre_completo() if self.jefe_area else "Ninguno\n"
     
     def obtener_empleados(self):
          return [empleado.nombre_completo() for empleado in self.empleados]
     
     def obtener_informacion(self):
          empleados_str = ", ".join(self.obtener_empleados()) or "Ninguno\n"
          jefe_str = self.obtener_jefe_area()
          return f"Área: {self.__nombre}, Descripción: {self.__descripcion}\nJefe de Área: {jefe_str}, Empleados: {empleados_str}\n"

## Insertando datos de empleados 
empleado_01 = Empleado("Jhon", "Martinez", 37, 1387990, "10543765", "2021-03-18")
empleado_02 = Empleado("Lorena", "Penagos", 26, 1879650, "67054098", "2018-09-14")
empleado_03 = Empleado("Pablo", "Londra", 32, 2570870, "1130765498", "2016-05-19")
empleado_04 = Empleado("Sandra", "Giraldo", 25, 1870950, "87654324", "2014-08-30")
empleado_05 = Empleado("Chistian", "Palacios", 28, 2570860, "1130765876", "2016-07-15")
empleado_06 = Empleado("Aura", "Mosquera", 29, 1570870, "34567092", "2015-05-16")
empleado_07 = Empleado("Carlos", "Salazar", 38, 3270650, "8769735", "2019-04-15")
empleado_08 = Empleado("Alejandra", "Balanta", 23, 1650890, "1140654328", "2018-09-30")

## Insertando datos de algunos jefes
jefe_01 = Jefe("Mauricio", "Castro", 49, 6570860, "12765439", "2008-03-15")
jefe_01.insertar_empleado(empleado_01)
jefe_01.insertar_empleado(empleado_02)
jefe_01.insertar_empleado(empleado_03)
jefe_01.insertar_empleado(empleado_04)

jefe_02 = Jefe("Francisco", "Gil", 53, 6570980, "67543879", "2009-05-15")
jefe_02.insertar_empleado(empleado_05)
jefe_02.insertar_empleado(empleado_06)
jefe_02.insertar_empleado(empleado_07)
jefe_02.insertar_empleado(empleado_08)

## Insertando datos de algunas áreas
area_01 = Area("Área de Marketing", "Esta área es la encargada de investigar al mercado objetivo del negocio, realizar estrategias de comunicación y publicidad en diversos canales y formatos y, de esta manera, potenciar la imagen positiva de la compañía")
area_01.insertar_empleado(Jefe)
area_01.insertar_empleado(empleado_01)
area_01.insertar_empleado(empleado_02)
area_01.designar_jefe(Jefe)

area_02 = Area("Investigación y Desarrollo", "Esta área es la encargada de realizar investigaciones sobre nuevos productos y servicios que la empresa puede ofrecer a su mercado objetivo.")
area_02.insertar_empleado(Jefe)
area_02.insertar_empleado(empleado_03)
area_02.insertar_empleado(empleado_04)
area_02.designar_jefe(Jefe)

## Obteniendo información de empleados, sueldos, jefes y áreas
print(empleado_01.obtener_informacion_empleados())
print(empleado_02.obtener_informacion_empleados())
print(empleado_03.obtener_informacion_empleados())
print(empleado_04.obtener_informacion_empleados())

print(empleado_01.obtener_sueldo())
print(empleado_02.obtener_sueldo())
print(empleado_07.obtener_sueldo())
print(empleado_08.obtener_sueldo())
print(Jefe.obtener_informacion_empleados())
print(Area.obtener_informacion())

print(empleado_01.obtener_sueldo)
print(empleado_02.obtener_sueldo)
print(Jefe.obtener_sueldo())

## Eliminando empleados
Area.suprimir_empleado(empleado_01)
Jefe.suprimir_empleado(empleado_05)
