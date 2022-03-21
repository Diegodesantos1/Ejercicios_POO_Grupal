<h1 align="center">Herencias POO</h1>

*Hemos usado la Programación Orientada a Objetos para resolver estos ejercicios.*

---

En este [repositorio](https://github.com/Diegodesantos1/Ejercicios_POO_Grupal) quedan resueltos los ejercicios de herencias en Python. Para llevar a cabo el proyecto nos hemos documentado a través de la teoría que se encuentra en el campus virtual y de otros medios.

***

## Integrantes

1. [@jmedina28](https://github.com/jmedina28)
2. [@mat0ta](https://github.com/mat0ta)
3. [@xavitheforce](https://github.com/Xavitheforce)
4. [@ESTHERRODRIGUEZGARCIA](https://github.com/ESTHERRODRIGUEZGARCIA)
5. [@Diegodesantos1](https://github.com/Diegodesantos1)

***

## Índice
1. [Ejercicio A: Herencia simple ](#id1)
2. [Ejercicio B: Puzzle](#id2)
3. [Ejercicio C: Herencia múltiple - Diamante](#id3)
4. [Ejercicio D: Herencia múltiple - Caso real](#id4)
***
## Ejercicios

### Ejercicio A: Herencia simple<a name="id1"></a>

Enunciado: Definir una clase Punto2D que tenga dos atributos x e y, y que implemente un método de traslación() que reciba como parámetro las dos componentes horizontal y vertical de la traslación, y modifique las coordenadas del punto en cuestión según el principio de que una traslación (a, b) consiste en sumar a (respectivamente b), al componente x (respectivamente y) de un punto.

Enunciado: Ahora añada la gestión de un punto en tres dimensiones, según los mismos principios que el punto 2D. Nota: esta adición se debe realizar sin acceder directamente a los componentes x e y del punto 3D.


```python
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

```

### Ejercicio B: Puzzle<a name="id2"></a>

Enunciado: ¿qué muestra este programa en la salida estándar?

```python
class Base: 
 
    def __init__(self): 
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        print(self.b) 
 
    def C(self): 
        print(self.c) 
 
class Derivada(Base): 
 
    def __init__(self): 
        self.a = "aa" 
        super().__init__() 
        self.c = "cc" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        self.b = "bb" 
        super().B() 
        print(self.b) 
 
base = Base() 
derivada = Derivada() 
 
base.A() 
derivada.A() 
print() 
base.B() 
derivada.B() 
base.C() 
derivada.C() 
derivada = base 
derivada.C() 
```
Salida estándar:

<br>
<img height="225" src="imagenes/salidaestandar.png" />
<br>
