def remover_repeticoes(lista):
    if len(lista) == 0:
        return Exception
    lista_sem_repeticoes = []
    for elemento in lista:
        if elemento not in lista_sem_repeticoes:
            lista_sem_repeticoes.append(elemento)
    return lista_sem_repeticoes

assert remover_repeticoes([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3]
assert remover_repeticoes([]) == Exception

print('Testes ok!')