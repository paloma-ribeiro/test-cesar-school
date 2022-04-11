"""
Use a palavra recebida na primeira questão e substitua:
- toda letra 'a' pelo numeral 4,
- toda letra 'i' pelo numeral 1,
- toda letra 'e' pelo numeral 3 e imprima o resultado.
Se a palavra for cadeira deve-se imprimir c4d31r4
"""


def ask_name_object() -> str:
    name = input('Insira o nome do objeto: ')
    return name


def replace_word(word: str) -> str:
    word = word.lower()
    new_word = word.replace('a', '4').replace('i', '1').replace('e', '3')

    print(new_word)


replace_word(ask_name_object())
