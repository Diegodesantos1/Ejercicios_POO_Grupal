
class Pared:
    pared=int(input("¿Cuántas paredes tiene la casa?"))
    def __init__(self,pared):
        self.pared=pared

class Ventana:
    ventana=int(input("¿Cuántas ventanas tiene la casa?"))
    def __init__(self,ventana):
        self.ventana=ventana

class Casa:
    def __init__(self,casa):
        self.casa=casa
class Superficie:
    def calcular():
        pared_norte = Pared("NORTE")
        pared_oeste = Pared("OESTE")
        pared_sur = Pared("SUR")
        pared_este = Pared("ESTE")
        ventana_norte = Ventana(pared_norte, 0.5)
        ventana_oeste = Ventana(pared_oeste, 1)
        ventana_sur = Ventana(pared_sur, 2)
        ventana_este = Ventana(pared_este, 1)
        casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
        print(casa.superficie_acristalada())

Superficie.calcular()
