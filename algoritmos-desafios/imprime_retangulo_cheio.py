coluna = int(input())
linha = int(input())
i = 0
j = 0

while i < linha:
    while j < coluna:
        print('#', end='')
        j += 1
    print()
    j = 0
    i += 1
