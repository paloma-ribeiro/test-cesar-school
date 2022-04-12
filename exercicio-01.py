"""
Peça o nome de um objeto para o usuário. Enquanto a palavra inserida
for menor que 4 letras ou maior que 8 letras, imprima "Palavra inválida" e peça
o nome do objeto novamente. Caso a palavra seja entre 4 a 8 letras, imprima "Palavra válida".
"""


def ask_name_object() -> str:
    name = input('Insira o nome do objeto: ')
    return name


def validate_name_object() -> str:
    while True:
        text = ask_name_object()
        if 4 <= len(text) <= 8:
            print('Palavra válida')
            return text
        print('Palavra inválida')


validate_name_object()
