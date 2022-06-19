import os
import formulas

lista_tabla_multiplicar = []
x = formulas.solicitar_numero()
for i in range(10):
    y = f"{i+1} x {x} = {(i+1)*x}\n"
    lista_tabla_multiplicar.append(y)
archivo = open(f'./archivo{x}.txt','w')
texto = lista_tabla_multiplicar
archivo.writelines(texto)
archivo.close()
lista_tabla_multiplicar = []