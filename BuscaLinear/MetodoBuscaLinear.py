# Método Busca linear em uma lista em alocação sequencial

def busca(lista, elem):
    """Retorna o índice elemento se ele estiver na lista ou None, caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None


lista_teste = [8, "5", 32, 0, "python", 11]
elemento = "python"

indice = busca(lista_teste, elemento)
if indice is not None:
    print("O índice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não se encontra na lista".format(elemento))
