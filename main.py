
def elegir():
    variable = int(input("\nConceptos de la POO en Python. Ejercicios de Herencias. \nPor favor, introduzca qué ejercicio desea realizar (1, 2, 3 o 4): \n"))

    if variable == 1:
        from Clases import herencia_simple
    elif variable == 2:
        from imagenes import salidaestandar
    elif variable == 3:
        from Clases import herencia_multiple_diamantes
    elif variable == 4:
        from Clases import herencia
    else:
        print("Sólo son válidos los valores 1, 2, 3 y 4.")
        elegir()
elegir()

if __name__ == "main":
    main()

