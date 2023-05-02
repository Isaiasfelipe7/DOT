""" Lista3_q16. Faça uma função que leia um número não determinado de valores positivos
e retorna a média aritmética dos mesmos.
"""

def calcular_media(lista):
    if len(lista) == 0: # Testar se a lista é vazia
        return Exception
    
    som = 0
    for i in range(len(lista)):
        if type(lista[i]) != int or lista[i] < 0: # Testar se algum valor da lista 
            return Exception                      # não é inteiro ou é negativo.
        som += lista[i]
    return som / len(lista)

assert calcular_media([1, 2, 4, 5]) == 3
assert calcular_media([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert calcular_media([10]) == 10
assert calcular_media([10, 5.4]) == Exception
assert calcular_media([-1]) == Exception
assert calcular_media([]) == Exception
assert calcular_media([-2, 3]) == Exception
assert calcular_media(['*', 5]) == Exception

print('Todos testes ok!')