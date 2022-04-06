"""
Taller 6
Problema 1
Bianca
La temperatura de un horno puede variar desde 0 hasta 100 grados centígrados y se clasifica de
acuerdo a lo siguiente:
MUY ALTA: si su valor esta entre 90 y 100
ALTA: si su valor esta entre 80 y 89
NORMAL: si su valor esta entre 40 y 79
BAJA: si su valor esta entre 0 y 39
Construya un programa que de acuerdo a la temperatura ingresada nos diga a que clasificación
pertenece.
"""

# ----------------------Clase Horno----------------------------------------------------------

class Horno:

    def __init__(self, grados):

        self.grados = grados
        self.temperatura = "x"


    def tomartemperatura(self):

        if self.grados >= 90 and self.grados <= 90:
            self.temperatura = "Muy Alta"

        elif self.grados >= 80 and self.grados <= 89:
            self.temperatura = "Alta"

        elif self.grados >= 40 and self.grados <= 79:
            self.temperatura = "Normal"

        elif self.grados >= 0 and self.grados <= 39:
            self.temperatura = "Baja"

        return self.temperatura


# --------------------------------------------------------------------------------------------------------


try:

    print("\nPrograma de temperaturas\n")

    grad = int(input("Ingrese a cuantos grados esta el horno "))

    instancia = Horno(grad)

    print("Pertenece a la clasificacion: ", instancia.tomartemperatura())

except:
    print("\nError de Valor ⚑ \n\n\nPara mas informacion consultar con\nBichicode🍑")


