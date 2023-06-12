''' Lista4_q7. Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False
'''

def mais_de_uma_vez(lista):
    if len(lista) == 0:
        return Exception
    
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return Exception
        
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[j] == lista[i] and j != i:
                return True
    return False

assert mais_de_uma_vez([10, 5.4]) == Exception
assert mais_de_uma_vez([]) == Exception
assert mais_de_uma_vez(["*", 5]) == Exception
assert mais_de_uma_vez([1, 2, 3, 1]) == True
assert mais_de_uma_vez([1, 2, 3]) == False
assert mais_de_uma_vez([1, 2, 3, 4, 1, 2]) == True

print('Testes ok!')
