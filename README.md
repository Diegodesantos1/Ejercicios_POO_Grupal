<h1 align="center">Ejercicios de POO Grupal</h1>

*Hemos usado la Programación Orientada a Objetos para resolver estos ejercicios.*

***

<h2>Repositorio</h2>

Este es el link del [Repositorio](https://github.com/Diegodesantos1/Ejercicios_POO_Grupal)

***

<h2>Integrantes</h2>

1. [Juan](https://github.com/jmedina28)
2. [Martín](https://github.com/mat0ta)
3. [Javier](https://github.com/Xavitheforce)
4. [Esther](https://github.com/ESTHERRODRIGUEZGARCIA)
5. [Diego](https://github.com/Diegodesantos1)

***


<h3>Ejercicio B: Puzzle</h3>

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
