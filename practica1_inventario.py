#--------------------------------------------INVENTARIO----
import numpy as np
contenido=np.zeros((3,1))
class inventario():
    def __init__(self):
        pass
    def meter(self,cantidad):
        nombre=int(input("Elije que objeto deseas agregar:\n\t1. lapiz\n\t2. pluma\n\t3. cuaderno\n"))
        if(nombre==1):
            contenido[0]=contenido[0]+x
        if(nombre==2):
            contenido[1]=contenido[1]+x
        if(nombre==3):
            contenido[2]=contenido[2]+x
        return(contenido)
    def sacar(self,cantidad):
        nombre=int(input("Elije que objeto deseas retirar:\n\t1. lapiz\n\t2. pluma\n\t3. cuaderno\n"))
        if(nombre==1):
            if(x>contenido[0]):
                print("La cantidad que desea retirar es mayor al contenido en el inventario")
            elif(contenido[0]>x):
                contenido[0]=contenido[0]-x
        if(nombre==2):
            if(x>contenido[1]):
                print("La cantidad que desea retirar es mayor al contenido en el inventario")
            elif(contenido[1]>x):
                contenido[1]=contenido[1]-x
        if(nombre==3):
            if(x>contenido[2]):
                print("La cantidad que desea retirar es mayor al contenido en el inventario")
            elif(contenido[2]>x):
                contenido[2]=contenido[2]-x
        return(contenido)
    def consultar(self):
        print("Hay "+str(contenido[0])+" lapices\n"+"Hay "+str(contenido[1])+" plumas\n"+"Hay "+str(contenido[2])+" cuadernos\n")

objeto1=inventario()
while (True):
    a=0
    opcion=int(input("Elije que accion quieres realizar:\n\t1. agregar al inventario\n\t2. retirar del inventario\n\t3. consultar el inventario\n"))
    if(opcion==1):
        x=int(input("Ingrese cantidad de que desea agregar al inventario: "))
        a=objeto1.meter(x)
    elif(opcion==2):
        x=int(input("Ingrese cantidad de que desea retirar del inventario: "))
        a=objeto1.sacar(x)
    elif(opcion==3):
        a=objeto1.consultar()
    else:
        print("Opcion no valida")
    salir=input("¿Desea hacer otra operacion?\n\ts=si\n\tn=no\n")
    if(salir=="n"):
        print("Hasta luego")
        break