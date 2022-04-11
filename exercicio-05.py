"""
Crie uma função que recebe uma string com varias palavras separadas por virgula.
Transforme essa string em uma lista de palavras.

"varias,palavras,separadas,por,virgula" deve virar ["varias","palavras","separadas","por","virgula"]

filtre essa lista, removendo as palavras começadas por 'p' ou terminadas em 's'.

Das palavras restantes, some o tamanho de cada palavra e imprime o resultado dessa soma
"""


def count_words(string: str) -> int:
    count = 0
    string = string.lower()
    string = string.split(',')

    new_string = list(filter(lambda x: x[0] != 'p' and x[-1] != 's', string))

    for i in new_string:
        for j in i:
            count += 1

    return count


# Test 1
phrase1 = 'varias,palavraS,separadas,Por,virgula'
print(count_words(phrase1))

# Test 2
phrase2 = 'maria,comprou,varias,saladas,e,palitos'
print(count_words(phrase2))
