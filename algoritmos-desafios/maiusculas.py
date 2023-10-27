def maiusculas(frase):
    maiusculas = ''
    frase = list(frase.replace(' ', ''))
    for let in frase:
        cod = ord(let)
        if cod >= 65 and cod <= 90:
            maiusculas += let
    return maiusculas
