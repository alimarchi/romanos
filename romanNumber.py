from typing import Type
from romanos import arabigo_a_romano, romano_a_arabigo

class RomanNumber():
    def __init__(self, entrada):
        if isinstance(entrada, str):
            self.arabigo = romano_a_arabigo(entrada)
            self.romano = entrada
        elif isinstance(entrada, int):
            self.romano = arabigo_a_romano(entrada)
            self.arabigo = entrada
        else:
            raise TypeError("La entrada tiene que ser entero o cadena")

    def __repr__(self):
        return self.romano

    def __int__(self):
        return self.arabigo

    def __lt__(self, entrada):
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")

        return self.arabigo < entrada.arabigo

    def __le__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("entrada tiene que ser romano")

        return self.arabigo <= other.arabigo

    def __eq__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("entrada tiene que ser romano")

        return self.arabigo == other.arabigo

    def __ne__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("entrada tiene que ser romano")

        return self.arabigo != other.arabigo

    def __ge__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("entrada tiene que ser romano")

        return self.arabigo >= other.arabigo

    def __gt__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("entrada tiene que ser romano")

        return self.arabigo > other.arabigo

    def __add__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("entrada tiene que ser romano")

        suma = self.arabigo + other.arabigo
        resultado = RomanNumber(suma)
        return resultado
            


