def bitcoin():
    try:
        x = int(input("ingrese el importe de bitcoin que posee: "))
        if x<=0:
            print("el importe debe ser mayor a cero")
            return bitcoin()
        else:
            return x
    except ValueError:
        print("no ingresaste un valor correcto, vuelve a intentarlo")
        return bitcoin()

import requests

def cambio():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    pagina = requests.get(url).json()
    tipo_cambioUSD = pagina['bpi']['USD']['rate_float']
    valor_b = bitcoin()
    valor_USD = tipo_cambioUSD * valor_b
    print (f"el importe en dolares es igual a ${valor_USD:,.4f}")

cambio()