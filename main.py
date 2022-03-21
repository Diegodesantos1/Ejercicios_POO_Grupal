
def elegir():
    variable = int(input("\nConceptos de la POO en Python. Ejercicios de Herencias. \nPor favor, introduzca qué ejercicio desea realizar: \n --> 1: Herencia simple\n --> 2: Salida éstandar\n --> 3: Herencia múltiple (diamante)\n --> 4: Herencia múltiple (casa)\n"))
    if variable == 1:
        from Clases import herencia_simple
    elif variable == 2:
        from imagenes import salidaestandar
    elif variable == 3:
        from Clases import herencia_multiple_diamante
    elif variable == 4:
        from Clases import herencia
    else:
        print("Sólo son válidos los valores 1, 2, 3 y 4.\n")
        elegir()
elegir()

if __name__ == "main":
    main()

