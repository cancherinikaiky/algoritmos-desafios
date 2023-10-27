def multiplica_matrizes(A, B):
    linhas_a, colunas_a = len(A), len(A[0])
    linhas_b, colunas_b = len(B), len(B[0])
    matriz_multiplicada = []
    
    if colunas_a == linhas_b:
        for lin in range(linhas_a):
            linha = []
            for col in range(colunas_b):
                multiplicacao = (A[col][lin]) * (B[lin][col])
                linha.append(multiplicacao)
            matriz_multiplicada.append(linha)
    
    return matriz_multiplicada

if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    B = [
        [1, 2],
        [4, 2, 2]
    ]
    
    print(multiplica_matrizes(A, B))