''' Lista4_q4. Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
-6, 4, 1] = 34
'''

def soma_qualquer_segmento(lista):
    if len(lista) == 0:
        return Exception
    
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return Exception
    
    soma = lista[0]
    soma_max = lista[0]
    for i in range(1, len(lista)):
        if soma + lista[i] > lista[i]:
            soma += lista[i]
            if soma > soma_max:
                soma_max = soma
        elif soma + lista[i] < lista[i]:
            soma = lista[i]
            if soma > soma_max:
                soma_max = soma
    return soma_max

assert soma_qualquer_segmento([]) == Exception
assert soma_qualquer_segmento([5, -2, -2, -7, 3, 15, 10, -3, 9,
-6, 4, 1]) == 34

print('Testes ok!')
