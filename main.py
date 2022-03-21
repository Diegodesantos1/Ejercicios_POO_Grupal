

def elegir():
    print("Si desea ver la resolución del ejercicio 2 acceda a la carpeta imágenes.  ")
    variable = int(input("Ejercicios de Herencias. Por favor, introduzca qué ejercicio desea realizar (1,3 o 4): "))

    if variable == 1:
        from Clases import herencia_simple
    elif variable == 3:
        from Clases import herencia_multiple_diamante
    elif variable == 4:
        from Clases import herencia
    else:
        print("Sólo son válidos los valores 1,3 y 4. ")
elegir()

if __name__ == "main":
    main()

