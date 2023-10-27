def insertion_sort(lista):
    fim = len(lista)
    i = 1
    while i < fim:
        x = lista[i]
        j = i - 1 
        while j >= 0 and lista[j] > x:
            lista[j + 1] = lista[j] 
            j -= 1 
            
        lista[j + 1] = x
        i += 1
    return lista
