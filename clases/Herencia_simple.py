class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mostrar(self.x, self.y)
        

    def mostrar(self, a, b):
        return "X: "+str(a), "Y: "+str(b)


    def traslacion(self, a, b):
        self.x += a
        self.y += b
        return self.x, self.y

a = Punto2D(3, 6)
print("A = {}".format(a))
 