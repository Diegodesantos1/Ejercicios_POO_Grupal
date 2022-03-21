#main
variable = int(input("Conceptos de la POO en Python. Ejercicios de Herencias. /nPor favor, introduzca qué ejercicio desea realizar (1, 2 o 3): "))

if variable == 1:
    from Clases import herencia_multiple_diamante
elif variable == 2:
    from Clases import herencia_simple
elif variable == 3:
    from Clases import herencia
else:
    print("Sólo son válidos los valores 1, 2 y 3. ")

if __name__ == "main":
    main()

