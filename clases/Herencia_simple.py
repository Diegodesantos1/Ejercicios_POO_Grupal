class Punto2D: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        return "X: "+str(self.x)+"; Y: "+str(self.y)

    def traslacion(self, a, b):
        self.x += a
        self.y += b
        return self.x, self.y

class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def mostrar(self):
        return "X: "+str(self.x)+"; Y: "+str(self.y)+"; Z: "+str(self.z)

    def traslacion(self, a, b, c):
        self.x += a
        self.y += b
        self.z += c
        return self.x, self.y, self.z

a = Punto2D(1, 2) 
print("A = {}".format(a.mostrar()))
 
a.traslacion(-1, -2) 
print("A = {}".format(a.mostrar()))
 
b = Punto2D(-3, 0) 
b.traslacion(5, -1) 
print("B = {}".format(b.mostrar()))

c = Punto3D(1,5,-3) 
c.traslacion(0, -2, 1) 
print("C = {}".format(c.mostrar()))