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

assert maior_soma([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 25
print('Testes ok!')
