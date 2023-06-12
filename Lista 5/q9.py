''' Lista5_q9. Escreva uma função chamada "encontrar_elemento_repetido" que receba uma lista de
números como parâmetro e retorne o elemento que se repete mais vezes na lista.
'''

def encontrar_elemento_repetido(lista):
    if len(lista) == 0:
        return Exception
    
    for i in lista:
        if type(i) != int and type(i) != float:
            return Exception
        
    contador = {}
    for num in lista:
        if num not in contador:
            contador[num] = 1
        else:
            contador[num] += 1
    
    num_repetido = None
    num_ocorr = 0

    for num, cont in contador.items():
        if cont > num_ocorr:
            num_ocorr = cont
            num_repetido = num

    return num_repetido if num_ocorr > 1 else Exception


assert encontrar_elemento_repetido([]) == Exception
assert encontrar_elemento_repetido(['s', 2]) == Exception
assert encontrar_elemento_repetido(['']) == Exception
assert encontrar_elemento_repetido([-1, -65.34, -34, -34]) == -34
assert encontrar_elemento_repetido([1, 7, 7, 9, 0, 0, 0]) == 0
assert encontrar_elemento_repetido([14, 38, 75, 90, 14, 6, 75, 75, 14, 8, 14]) == 14

print('Testes ok!')


