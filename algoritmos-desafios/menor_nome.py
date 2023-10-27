def formatar(str):
    return str.strip(' ').capitalize()

def menor_nome(str_list):
    str_list = list(map(formatar, str_list))
    
    return sorted(str_list, key=lambda x: len(x))[0]
