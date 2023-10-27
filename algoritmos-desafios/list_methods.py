# ORDENA UMA LISTA DECRESCENTEMENTE 
my_list = [1, 2, 3]
my_list_reverse = reversed(my_list)
print(my_list)  # Output: [3, 2, 1]

# ORDENA UMA LISTA CRESCENTEMENTE 
my_list = [3, 1, 2]
my_list_sort = sorted(my_list)
print(my_list)  # Output: [1, 2, 3]

# VERIFICA QUANTAS VEZES UM ELEMENTO EXISTE NA LISTA
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2

# RETORNA O ELEMENTO À PARTIR DE UM ÍNDICE
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1

# REMOVE UM ELEMENTO DA LISTA À PARTIR DO ÍNDICE
my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(popped_element)  # Output: 2
print(my_list)  # Output: [1, 3]

# FILTRA UMA LISTA E REMOVE TODOS ELEMENTOS QUE A FUNÇÃO DENOMINAR
my_list = [1, 2, 3, 4, 5]
my_list = list(filter(lambda x: x != 3, my_list))  # Remove o elemento 3
print(my_list)  # Output: [1, 2, 4, 5]

# INDICA PRIMEIRO A POSIÇÃO, E DEPOIS O NÚMERO QUE SERÁ INSERIDO NELA
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]

# ADICIONA OS ELEMENTOS DE UMA LISTA NO FIM DE OUTRA LISTA
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5]

# ADICIONA UM ITEM NO FIM DA LISTA
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

