coluna = int(input())
linha = int(input())
i = 0
j = 0

while i < linha:
    if i > 0 and i <= linha - 2:
        while j < coluna:
            if j > 0 and j <= coluna - 2:
                print(' ', end='')
            else:
                print('#', end='')
            j += 1
    else:
        while j < coluna:
            print('#', end='')
            j += 1
    print()
    j = 0
    i += 1