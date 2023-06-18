''' Lista4_q8. Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5
'''

def mais_proximo(lista):
    if len(lista) == 0:
        return Exception

    for i in range(len(lista)):
        if type(lista[i]) != float and type(lista[i]) != int:
            return Exception
    
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    
    media = soma / len(lista)
    menor_diferenca = abs(media - lista[0])

    for i in range(1, len(lista)):
        if abs(media - lista[i]) < menor_diferenca:
            menor_diferenca = abs(media - lista[i])
            valor = lista[i]
    if len(lista) == 1:
        return lista[0]
    else:
        return valor


assert mais_proximo([]) == Exception
assert mais_proximo(["*", 2, 8.9, 2]) == Exception
assert mais_proximo([2]) == 2
assert mais_proximo([1, 3.5, 8, 4.3]) == 4.3
assert mais_proximo([2.5, 7.5, 10.0, 4.0]) == 7.5

print('Testes ok!')
