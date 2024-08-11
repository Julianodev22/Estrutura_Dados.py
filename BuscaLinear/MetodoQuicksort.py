
def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        # Recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p-1)
        # Recursivamente na sublista à direita (maiores)
        quicksort(lista, p+1, fim)


def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        # j Sempre avança, pois representa o elementa em análise
        # e Delimita os elementos maiores que o pivô
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            # Incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i
