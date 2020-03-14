# -*- coding utf8 -#-

import random
import sys
import datetime
import platform

   

class MenuEstacionamiento():
    def menu():
        """ MENU para ingresar los datos """
    def __init__(self):
        """ OPciones """
        self.Vehiculo = list()
        self.opciones = {
            "1":self.VehiculosTotales,
            "2":self.Ganancias,
            "3":self.Salir
        }
        
    def mostrar_Menu(self):
        """el menu se desplegara a continucacion"""
        print("""
              MENU
              1) Vehiculos Totales
              2)Grnancias
              3)SALIR
              """)
    
    def totalVehiculos(self):
     
        for vehiculo_ in Vehiculo:
            print("vehiciculos totales", vehiculo)
        
    def salir(self):
        sys.exit()
        
class Vehiculos():
    
    def __init__(self):
        self.numeroPlaca
        self.marca
        self.modelo
        self.tipoVehiculo
        self.horaIngreso
        self.estado = True        
        self.fraccion
    def automovil(self):
        tarija1 = 20
        if hora_Ingreso > hora_salida:
            fraccion=hora_Ingreso+tarija1
            print("PAGA UNA FRACCION DE", fraccion)
        else:
            print("SIN FRACCION")
        
    def motocicleta(self):
        tarija2 = 10


print(input(numero_placa("ingrese el numero de placa ")))
numero_placa = 1234
marca_ = "Toyota"
modelo_ = "turismo"
tipo_Vehiculo = "turismo"
hora_Ingreso = datetime
hora_salida= 0