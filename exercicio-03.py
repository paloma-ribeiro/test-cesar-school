"""
Crie uma função que recebe um número como parâmetro. A função deve
calcular e retornar o fatorial desse número.

4! = 4*3! = 4*3*2*1

7! = 7*6! = 7*6*5*4*3*2*1
"""


def factorial(number: int) -> int:
    numbers = []
    product = 1

    for i in range(1, number + 1):
        numbers.append(i)

    for i in numbers:
        product *= i

    return product


print(factorial(4))
print(factorial(7))
