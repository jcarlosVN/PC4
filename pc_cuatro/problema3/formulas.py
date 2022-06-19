import random
from pyfiglet import Figlet
figlet=Figlet()
fuente = figlet.getFonts()


def escoger_opcion():
    try:
        x = int(input("ingrese 1 si desea escoger una fuente o 2 si desea una fuente aleatorea: "))
        if x==1:
            return escoger_fuente()
        elif x==2:
            return aleatorio_fuente()
    except ValueError:
        print("no ingresaste un valor correcto, vuelve a intentarlo")
        return escoger_opcion()


def escoger_fuente():
    try:
        x = str(input("ingrese una fuente a utilizar: "))
        if x in fuente:
            return x
        else:
            print(f"esa fuente no existe, vuelve a intentarlo")
            return escoger_fuente()
    except ValueError:
        print("no ingresaste un valor correcto, vuelve a intentarlo")
        return escoger_fuente()


def aleatorio_fuente():
    fuente_random = random.choice(fuente)
    return fuente_random


def escoger_texto():
    x = str(input("ingrese el texto: "))
    return x