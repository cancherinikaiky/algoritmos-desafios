def ternaria(num):
    base = 3
    j = len(num)
    resultado = 0
    for i, e in enumerate(num):
        j -= 1
        resultado += e * (base ** j)
    
    return resultado

def main():
    while True:
        try:
            num = [int(num) for num in input()] # 123 vira [1, 2, 3]
        except EOFError:
            break
main()