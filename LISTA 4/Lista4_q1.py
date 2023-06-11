'''' Lista4_q1. Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]
'''

def remover_repeticoes(lista):
    if len(lista) == 0:
        return Exception
    
    for i in lista:
        if type(i) != int:
            return Exception
        
    lista_sem_repeticoes = []
    for elemento in lista:
        if elemento not in lista_sem_repeticoes:
            lista_sem_repeticoes.append(elemento)
    return lista_sem_repeticoes

assert remover_repeticoes([]) == Exception
assert remover_repeticoes(["*", 3, 5, 5]) == Exception
assert remover_repeticoes([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3]

print('Testes ok!')
