valores_romanos = {
    1 : "I",
    4 : "IV",
    5 : "V",
    9 : "IX",
    10 : "X",
    40 : "XL",
    50 : "L",
    90 : "XC",
    100 : "C",
    400 : "CD",
    500 : "D",
    900 : "CM",
    1000: "M"
}

valores_arabigos = {v: k for k, v in valores_romanos.items()}

class RomanError(Exception):
    pass

def valida_numero(n):
    if not isinstance(n, int):
        raise TypeError(f"{n} deber ser de tipo int")

    if n <= 0:
        raise ValueError(f"{n} debe ser un entero positivo")

def arabigo_a_romano(n):
    valida_numero(n)
    romano = ""
    resto = None

    while resto != 0:
        for valor in sorted(valores_romanos.keys(), reverse=True):
            if n >= valor:
                break

        cociente = n // valor
        resto = n % valor
        romano += cociente * valores_romanos[valor]
        n = resto

    return romano



def romano_a_arabigo(cadena):
    resultado = 0
    cont_repeticiones = 0

    for ix in range(len(cadena)-1):
        letra = cadena[ix]
        siguiente = cadena[ix + 1]

        #comprobar repeticiones
        if letra == siguiente:
            cont_repeticiones += 1
        elif valores_arabigos[letra] < valores_arabigos[siguiente] and cont_repeticiones > 0:
            raise RomanError(f"Error de sintaxis. {letra} tras repeticiones no puede restar")
        else:
            cont_repeticiones = 0

        if letra in "VLD" and cont_repeticiones > 0 or cont_repeticiones > 2:
            raise RomanError(f"Error de sintaxis. Demasiadas repeticiones de {letra}") 
        

        if valores_arabigos[letra] >= valores_arabigos[siguiente]:
            resultado += valores_arabigos[letra]
        else:
            if letra in "VLD":
                raise RomanError("Error de sintaxis. {letra} no puede restar")
            resultado -= valores_arabigos[letra]

    resultado += valores_arabigos[cadena[len(cadena)-1]]

    return resultado
