''' Lista4_q3. Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
4, 1] = 25
'''

def maior_soma(lista):
    if len(lista) == 0:
        return Exception
    
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return Exception
    
    maior_soma = lista[0] + lista[1]
    for i in range(1, len(lista) -1):
        if lista[i] + lista[i+1] > maior_soma:
            maior_soma = lista[i] + lista[i+1]

    return maior_soma

assert maior_soma([]) == Exception
assert maior_soma(["y", 2, 1]) == Exception
assert maior_soma([5.4, 8.2, 8, 9, 10, 8.7, 20]) == Exception
assert maior_soma([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 25

print('Testes ok!')
