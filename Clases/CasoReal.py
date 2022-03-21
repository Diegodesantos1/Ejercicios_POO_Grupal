class Casa():
    def __init__(self):
      self.casa = {}
    def Paredes(self, orientacion):
      for i in range(len(orientacion)):
        nombre = orientacion[i]
        self.casa[nombre] = {
            'ventanas': {},
        }
      print(self.casa)
      Casa().Ventanas(self.casa, [['NORTE', 0.5], ['SUR', 1], ['ESTE', 2], ['OESTE', 1]])
    def Ventanas(self, casa, ventanas):
      dimensiones = []
      for i in range(len(ventanas)):
        nombre = ventanas[i][0]
        casa[nombre]['ventanas'] = {
          1: ventanas[i][1]
        }
        dimensiones.append(ventanas[i][1])  
      print(casa)
      Casa().Superficie(dimensiones)
      
    def Superficie(self, dimensiones):
      total = 0
      for i in range(len(dimensiones)):
        total += dimensiones[i]
      print('Superficie avristalada: ' + str(total))
   
  
# Casa().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE']) <-- Esto pal main