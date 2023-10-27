import math

def classifica_tripla(x, y, z):
    if math.gcd(x, y, z) == 1 and math.pow(x, 2) + math.pow(y, 2) == math.pow(z, 2):
        return 'tripla pitagorica primitiva'
    if math.pow(x, 2) + math.pow(y, 2) == math.pow(z, 2):
        return 'tripla pitagorica'
    return 'tripla'

def main():
    while True:
        try:
            x, y, z = sorted(list(map(int, input().split())))
            resultado = classifica_tripla(x, y, z)
            print(resultado)
        except EOFError:
            break
main()