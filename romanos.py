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
        raise TypeError("debe ser de tipo int")

    if n <= 0:
        raise ValueError("debe ser un entero positivo")

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

"""
def arabigo_a_romano_plus(n):
    if n < 4000:
        arabigo_a_romano(n)
    else:
        n = str(n)
        ultimos_numeros = int(n[-3:])
        len_primera_parte = len(n)-3
        primera_parte = int(n[:len_primera_parte])
        n = "(" + str(arabigo_a_romano(primera_parte)) + ")" + str(arabigo_a_romano(ultimos_numeros))
        
    return n

"""


def simbolo_a_valor(simbolo):
    try:
        return valores_arabigos[simbolo]
    except KeyError as el_error:
            raise RomanError("Error de sintaxis. Simbolo {} no permitidos".format(el_error))

def restar(letra, siguiente):
    if letra in "VLD":
        raise RomanError("Error de sintaxis. {} no puede restar".format(letra))
    elif letra == "I" and siguiente not in ("XV"):
        raise RomanError("Error de sintaxis. {}{} no puede restar".format(letra, siguiente))
    elif letra == "X" and siguiente not in ("LC"):
        raise RomanError("Error de sintaxis. {} {} no puede restar".format(letra, siguiente))
    elif letra == "C" and siguiente not in ("DM"):
        raise RomanError("Error de sintaxis. {}{} no puede restar".format(letra, siguiente))

def romano_a_arabigo(cadena):
    resultado = 0
    cont_repeticiones = 0
    cadena = cadena.upper()

    for ix in range(len(cadena)-1):
        letra = cadena[ix]
        siguiente = cadena[ix +1]
        valor = simbolo_a_valor(letra)
        siguiente_valor = simbolo_a_valor(siguiente)
        

        #comprobar repeticiones
        if valor == siguiente_valor:
            cont_repeticiones += 1
        elif valor < siguiente_valor and cont_repeticiones > 0:
            raise RomanError("Error de sintaxis. {} tras repeticiones no puede restar".format(letra))
        else:
            cont_repeticiones = 0

        if letra in "VLD" and cont_repeticiones > 0 or cont_repeticiones > 2:
            raise RomanError("Error de sintaxis. Demasiadas repeticiones de {}".format(letra)) 
        

        if valor >= siguiente_valor:
            resultado += valor
        else:
            restar(letra, siguiente)

            resultado -= valor

    resultado += simbolo_a_valor(cadena[-1])

    return resultado
