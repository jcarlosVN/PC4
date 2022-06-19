def solicitar_numero():
    try:
        x = int(input("ingrese un numero entero entre 1 y 10: "))
        if x<1 or x>10:
            print("el numero debe estar entre 1 y 10, vuelve a intentarlo")
            return solicitar_numero()
        else:
            return x
    except ValueError:
        print("no ingresaste un valor correcto, vuelve a intentarlo")
        return solicitar_numero()