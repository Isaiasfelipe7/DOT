''' Lista4_q6. Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False
'''

def verificar_ordem_ascendente(lista):
    if len(lista) == 0:
        return Exception
    
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return Exception
        
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True

assert verificar_ordem_ascendente([]) == Exception
assert verificar_ordem_ascendente([2.3, 3, 8.3, 10, ]) == Exception
assert verificar_ordem_ascendente([1, 2, 3]) == True
assert verificar_ordem_ascendente([3, 7, 2]) == False
assert verificar_ordem_ascendente([]) == Exception
assert verificar_ordem_ascendente([True, 12, 32]) == Exception
assert verificar_ordem_ascendente([2.5, 1, 25]) == Exception
assert verificar_ordem_ascendente(['a', 12]) == Exception
assert verificar_ordem_ascendente([1, 2, 3]) == True
assert verificar_ordem_ascendente([23, 34, 43]) == True
assert verificar_ordem_ascendente([1, -1, 20]) == False
assert verificar_ordem_ascendente([12, 11, 100]) == False
assert verificar_ordem_ascendente([-1, -2, -3, -4]) == False
assert verificar_ordem_ascendente([-8, -7, -6, -4, -3, -2]) == True
assert verificar_ordem_ascendente([1, 2, 2, 3, 3, 3, 3]) == True
assert verificar_ordem_ascendente([1, 45, 65, 65, 65, 65, 65, 65, 2]) == False

print('Testes ok!')
