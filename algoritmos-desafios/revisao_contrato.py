def corrigir(contrato):
    contrato = contrato.split(' ')
    contrato_corrigido = list(filter(lambda e: e != contrato[0], contrato[1]))
    contrato_corrigido = ''.join(contrato_corrigido)
    
    if contrato_corrigido.count('0') == len(contrato_corrigido):
        print('0')
    else:
        print(contrato_corrigido.lstrip('0'))
    
def main():
    while True:
        inp = input()
        if inp == 'algum comando q para o input':
            break
        ...
main()
