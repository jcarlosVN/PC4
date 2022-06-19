def numero_level():
    try:
        x = int(input("ingrese un numero entero: "))
        if x<=0:
            print("el numero debe ser mayor a cero")
            return numero_level()
        else:
            return x
    except ValueError:
        print("no ingresaste un valor correcto, vuelve a intentarlo")
        return numero_level()


def numero_juego(y):
    m = numero_level()
    if m < y:
        print("¡Demasiado pequeño!")
        return numero_juego(y)
    elif m > y:
        print("¡Te pasaste!")
        return numero_juego(y)
    else:
        print("¡Adivinaste!")