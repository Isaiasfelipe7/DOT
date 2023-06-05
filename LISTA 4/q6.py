def verificar_ordem_ascendente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

assert verificar_ordem_ascendente([1, 2, 3]) == True
assert verificar_ordem_ascendente([3, 7, 2]) == False

print('Testes ok!')
