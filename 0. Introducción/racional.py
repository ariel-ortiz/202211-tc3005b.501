from math import gcd
from functools import total_ordering

@total_ordering
class Racional:

    def __init__(self, numerador=0, denominador=1):
        if denominador == 0:
            raise ValueError('¡Denominador no puede ser cero!')
        signo = -1 if numerador * denominador < 0 else 1
        numerador = abs(numerador)
        denominador = abs(denominador)
        comun = gcd(numerador, denominador)
        self.__numerador = numerador // comun * signo
        self.__denominador = denominador // comun

    def __str__(self):
        return f'{self.__numerador}/{self.__denominador}'

    def __eq__(self, other):
        return (self.__numerador == other.__numerador
            and self.__denominador == other.__denominador)

    def __lt__(self, other):
        return (self.__numerador * other.__denominador
            < self.__denominador * other.__numerador)

    def __add__(self, other):
        return Racional(
            self.__numerador * other.__denominador
            + self.__denominador * other.__numerador,
            self.__denominador * other.__denominador)


a = Racional()
print(f'a:          {a}')
b = Racional(1, 2)
print(f'b:          {b}')
c = Racional(-3, -6)
print(f'c:          {c}')
print(f'b == c:     {b == c}')
print(f'a != b:     {a != b}')
print(f'b != c:     {b != c}')
print(f'a < b:      {a < b}')
print(f'b > a:      {b > a}')
print(f'b <= c:     {b <= c}')
print(f'a >= b:     {a >= b}')
d = Racional(1, 3)
print(f'd:          {d}')
e = b + d
print(f'e == b + d: {e}')
