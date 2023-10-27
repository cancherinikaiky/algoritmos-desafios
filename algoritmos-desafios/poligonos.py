def formar_poligono(x, y):
    i = 1
    while i <= x:
        if (y * i) % x == 0:
            return i
        i += 1

def main():
    n = int(input())
    for _ in range(n):
        x, y = list(map(int, input().split()))
        resultado = formar_poligono(x, y)
        print(resultado)
    
main()