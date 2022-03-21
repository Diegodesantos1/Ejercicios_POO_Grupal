#main
def elegir():
    variable = int(input("Conceptos de la POO en Python. Ejercicios de Herencias. /nPor favor, introduzca qué ejercicio desea realizar (1, 2, 3 o 4): "))

    if variable == 1:
        from Clases import herencia_simple
    if variable == 2:
        from imagenes import salidaestandar
    elif variable == 3:
        from Clases import herencia_multiple_diamantes
    elif variable == 3:
        from Clases import herencia
    else:
        print("Sólo son válidos los valores 1, 2 y 3. ")
elegir()

if __name__ == "main":
    main()

