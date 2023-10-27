def soma_matrizes(m1, m2):
    lin1 = len(m1)
    col1 = len(m1[0])
    
    lin2 = len(m2)
    col2 = len(m2[0])
    
    matriz_somada = []
    if lin1 == lin2 and col1 == col2:
        for i in range(lin1):
            linha = []
            for j in range(col1):
                linha.append(m1[i][j] + m2[i][j])
            matriz_somada.append(linha)
        return matriz_somada
    return False
    