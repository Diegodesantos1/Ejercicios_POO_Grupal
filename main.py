
def elegir():
    print("\nSi desea ver la salida estándar del ejercicio 2 acceda a la carpeta imágenes. ")
    variable = int(input("\nConceptos de la POO en Python. Ejercicios de Herencias. \n\nPor favor, introduzca qué ejercicio desea realizar: \n --> 1: Herencia simple\n --> 3: Herencia múltiple (diamante)\n --> 4: Herencia múltiple (casa)\n"))
    if variable == 1:
        from Clases import herencia_simple
    elif variable == 3:
        from Clases import herencia_multiple_diamante
    elif variable == 4:
        from Clases import herencia
    else:
        print("Sólo son válidos los valores 1,3 y 4.\n")
        elegir()
elegir()


