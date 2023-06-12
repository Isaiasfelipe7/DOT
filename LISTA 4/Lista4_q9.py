''' Lista4_q9. Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] =
[7, 3]
'''

def elimina_valores_repetidos(lista):
    if len(lista) == 0:
        return Exception
    
    for i in lista:
        if type(i) != int:
            return Exception
    nova_lista = []
    ocorrencias = {}
    for num in lista:
        if num not in ocorrencias:
            ocorrencias[num] = 1
        else:
            ocorrencias[num] += 1

    for num in lista:
        if ocorrencias[num] == 1:
            nova_lista.append(num)

    return nova_lista

assert elimina_valores_repetidos([]) == Exception
assert elimina_valores_repetidos(["*", 3, 9]) == Exception
assert elimina_valores_repetidos([5, 4, 5, 7, 3, 4]) == [7, 3]


print('Testes ok!')
