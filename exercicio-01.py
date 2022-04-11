"""
Peça o nome de um objeto para o usuário. Enquanto a palavra inserida
for menor que 4 letras ou maior que 8 letras, imprima "Palavra inválida" e peça
o nome do objeto novamente. Caso a palavra seja entre 4 a 8 letras, imprima "Palavra válida".
"""


def ask_name_object() -> str:
    name = input('Insira o nome do objeto: ')
    return name


def validate_name_object(name_object: str):
    x = True

    while x:

        if 4 < len(name_object) < 8:
            print('Palavra válida')
            break
        else:
            print('Palavra inválida')
            continue


name_obj = ask_name_object()
validate_name_object(name_obj)
