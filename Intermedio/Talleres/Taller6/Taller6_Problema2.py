"""
Taller 6
Problema 2

Se desea un programa que lea la cantidad de estudiantes de un salón de clases.
Para cada estudiante
el programa debe solicitar su sexo,
estatura
y peso.
Al finalizar el programa debe escribir la cantidad
de estudiantes que tiene el salón,
la cantidad de estudiantes por sexo,
promedio del peso por sexo y
el promedio de la estatura por sexo.
"""


import numpy

# ----------------------Clase Salon----------------------------------------------------------------


# Clase salon donde esta la informacion global
class Salon:

# Constructor
    def __init__(self, cantidad):

        self.calumnos = cantidad

        self.cfem = 0

        self.cmasc = 0

        self.pesofem = []

        self.pesomasc = []

        self.estfem = []

        self.estmasc = []


# Metodo que registra los datos de los varones
    def masculino(self, est, pes):

        self.cmasc += 1

        self.pesomasc.append(pes)

        self.estmasc.append(est)


# Metodo que registra los datos de las damas
    def femenino(self, est, pes):
        self.cfem += 1
        self.pesofem.append(pes)
        self.estfem.append(est)


# Metodo que calcula los promedios
    def promedios(self):

        # Si no hay alumnas los promedios son cero para evitar error de mean
        if  self.cfem == 0:
            pf = 0
            ef = 0

        else:
            pf = numpy.mean(self.pesofem)
            ef = numpy.mean(self.estfem)

        # Si no hay alumnos los promedios son cero para evitar error de mean
        if self.cmasc == 0:
            pm = 0
            em = 0

        else:
            pm = numpy.mean(self.pesomasc)
            em = numpy.mean(self.estmasc)

        return pf, pm, ef, em

# ----------------------Clase Estudiante----------------------------------------------------------------

# Clase Estudiante donde se registran los datos individuales
class Estudiante:

# Constructor de Estudiante
    def __init__(self, sexo, estatura, peso):

        self.sexo = sexo

        self.estatura = estatura

        self.peso = peso


# Metodo que clasifica la informacion segun sexo y la envia al Salon
    def medir(self):

        estatura1 = self.estatura

        peso1 = self.peso

        if self.sexo == "M" or self.sexo == "m":

            instancia.masculino(estatura1, peso1)

        else:

            instancia.femenino(estatura1, peso1)

# --------------------------------------------------------------------------------------------------------
try:
    print("\nPrograma de Estudiantes del Salon\n")

    cantidad = int(input("Cantidad de estudiantes: "))

    #Instanciando el salon
    instancia = Salon(cantidad)


    for i in range(cantidad):

        print("\nIngrese los datos del Alumno #", i+1)
        sexo = input("Ingrese M Para Sexo Masculino ♂ \nIngrese F para Sexo Femenino ♀: \n>>")
        estatura = float(input("Estatura: "))
        peso = int(input("Peso: "))

        # Instanciando el estudiante
        variable= Estudiante(sexo, estatura, peso)

        # llamada a la clasificacion por sexo
        variable.medir()

    # Llamada a los promedios
    pfem, pmas, efem, emas = instancia.promedios()

    print("\n\nCantidad de alumnos", cantidad,
          "\nPromedio peso femenino: ", pfem,
          "\nPromedio peso masculino", pmas,
          "\nPromedio estatura femenina", efem,
          "\nPromedio estatura masculina", emas)

# Cualquier error mostrara un mensaje
except:
    print("\nError de Valor ⚑ \n\n\nPara mas informacion consultar con\nBichicode🍑")
