def somar(a, b):
    return ((b - a + 1) * (a + b)) // 2
    

def main():
    while True:
        try:
            a, b = list(map(int, input().split()))
            resultado = somar(a, b)
            print(resultado)
        except EOFError:
            break
        
main()
    