def cortar(str):
    metade = len(str) // 2
    str_1 = list(str[:metade])
    str_2 = list(str[metade:])
    
    str_1.reverse()
    str_2.reverse()
    
    resultado = str_1 + str_2
    resultado = ''.join(resultado)
    return resultado

def main():
    n = int(input())
    for _ in range(n):
        frase = input()
        resultado = cortar(frase)
        print(resultado)
    
main()