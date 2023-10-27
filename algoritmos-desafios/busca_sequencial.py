def busca_sequencial(lista, x):
    for i, e in enumerate(lista):
        if e == x:
            return i
    return False