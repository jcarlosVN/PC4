import formulas
from pyfiglet import Figlet
figlet=Figlet()
fuente = figlet.getFonts()

def main():
    m = formulas.escoger_opcion()
    figlet.setFont(font=m)
    n = formulas.escoger_texto()
    print(f"la fuente es {m} y el texto final es: ")
    print(figlet.renderText(n))


main()