def bubble_sort(lista):
    fim = len(lista)
    
    for i in range(fim - 1, 0, -1):
        troca = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                troca = True
                print(lista)                
        if not troca:
            break
    return lista
