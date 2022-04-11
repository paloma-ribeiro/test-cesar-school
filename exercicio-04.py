"""
Crie uma função que recebe uma lista de números como parâmetro.
A função deve filtrar a lista para apenas números positivos,
em seguida deve remover os números repetidos e por fim imprimir a
média dos números restantes
"""


def list_filter(numbers: list) -> float:
    new_numbers = list(set(filter(lambda x: x >= 0, numbers)))
    average = sum(new_numbers) / len(new_numbers)

    return average


list_number = [1, 4, 4, 5, 7, 8, 8, -9, 0]
result = list_filter(list_number)
print(f'Média dos números: {result:.2f}')
