""" Lista4_q1. Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]
"""

def elimina_repeticoes(l1):
    l2 = []

    if len(l1) == 0: # testar se a lista é vazia
        return Exception
    
    for i in range(len(l1)):
        if type(l1[i]) != int: # testar se algum valor da lista não é inteiro
            return Exception
        if l1[i] not in l2: # incluir valor l1[i] na lista 2(l2) caso não exista.
            l2.append(l1[i])
        
    return l2

assert elimina_repeticoes([5, 4, 5, 7, 3, 4]) == ([5, 4, 7, 3])
assert elimina_repeticoes([10, 5.4]) == Exception
assert elimina_repeticoes([]) == Exception
assert elimina_repeticoes(["*", 5]) == Exception

print('Testes ok!')
