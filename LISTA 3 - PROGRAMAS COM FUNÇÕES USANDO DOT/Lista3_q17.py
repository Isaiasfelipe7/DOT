""" Lista3_q17. Faça uma função que lê 50 valores inteiros e retorna o maior e o menor deles.
"""

def maior_menor(lista):
    if len(lista) == 0:
        return Exception
    mai = 0
    men = 0
    for i in range(len(lista)):
        if type(lista[i]) != int or lista[i] < 0:
            return Exception
        if i == 0:
            mai = men = lista[i]
        else:
            if lista[i] > mai:
                mai = lista[i]
            if lista[i] < men:
                men = lista[i]
    return mai, men

assert maior_menor([2, 4, 19, 22]) == (22, 2)
assert maior_menor([1, 1, 1, 1, 1, 1]) == (1, 1)
assert maior_menor([47, 69, 77, 22, 120, 110]) == (120, 22)
assert maior_menor([562, 342, 81, 569, 122, 0]) == (569, 0)
assert maior_menor([]) == Exception
assert maior_menor([2.6, 2, 8.7, 9]) == Exception
assert maior_menor(['a', '*', 2, 2.9]) == Exception
assert maior_menor([-2, 3, 10, 120]) == Exception

print('Todos testes ok!')
