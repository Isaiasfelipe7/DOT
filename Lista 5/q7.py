''' Lista5_q7. Escreva uma função chamada "encontrar_elemento_faltante" que receba uma lista de
números de 1 a n (sendo n um número inteiro) em ordem aleatória, com um elemento
faltando, e retorne o elemento que está faltando. Ex: [4,3,1,5] = 2
'''

def encontrar_elemento_faltante(l):
    if type(l) != list or len(l) < 2:
        return Exception
    
    if (max(l) - len(l)) > 1 or (max(l) == len(l)):
        return Exception
    
    for i in range(1, max(l)):
        if i not in l:
            return i
        

assert encontrar_elemento_faltante('s') == Exception
assert encontrar_elemento_faltante([10]) == Exception
assert encontrar_elemento_faltante([]) == Exception
assert encontrar_elemento_faltante([4, 3, 1, 6]) == Exception
assert encontrar_elemento_faltante([1, 2, 3, 4,]) == Exception
assert encontrar_elemento_faltante([4, 3, 1, 5]) == 2
assert encontrar_elemento_faltante([3, 5, 2, 1, 7, 9,10, 8, 4]) == 6
assert encontrar_elemento_faltante([2, 5, 3, 7, 6, 9, 8, 4]) == 1

print('Testes ok!')
