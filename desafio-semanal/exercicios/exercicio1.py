# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a listapara um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.


def remove_duplicatas(lista):
    return list(set(lista))

lista = [1, 2, 3, 4, 2, 3, 5]
lista_sem_duplicatas = remove_duplicatas(lista)
print("Lista original:", lista)
print("Lista sem duplicatas:", lista_sem_duplicatas)
