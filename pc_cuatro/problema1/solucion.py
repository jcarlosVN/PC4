import random
import formulas

def main():
    x = formulas.numero_level()
    print(f"el nivel escogido es {x}")
    y = random.randint(1,x)
    print(f"se ha creado un valor aleatorio entre 1 y {x}, adivina el número: ")
    z = formulas.numero_juego(y)

main()