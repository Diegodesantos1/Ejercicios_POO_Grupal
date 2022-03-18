class Pared:
    def __init__(self,pared):
        self.pared=pared

class Ventana:
    def __init__(self,ventana,num_ventana):
        self.ventana=ventana
        self.num_ventana=num_ventana

class Casa:
    def __init__(self,casa,espacio):
        self.casa=casa
        self.espacio=espacio
    def definir(espacio):
        pared_norte = Pared("NORTE")
        pared_oeste = Pared("OESTE")
        pared_sur = Pared("SUR")
        pared_este = Pared("ESTE")
        espacio=[pared_norte, pared_oeste, pared_sur, pared_este]
        ventana_norte = Ventana(pared_norte, 0.5)
        ventana_oeste = Ventana(pared_oeste, 1)
        ventana_sur = Ventana(pared_sur, 2)
        ventana_este = Ventana(pared_este, 1)
    def superficie_acristalada(espacio):
        casa = Casa(espacio)
        print(casa.superficie_acristalada(espacio))
Casa.superficie_acristalada(espacio)

