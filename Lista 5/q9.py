''' Lista5_q9. Escreva uma função chamada "encontrar_elemento_repetido" que receba uma lista de
números como parâmetro e retorne o elemento que se repete mais vezes na lista.
'''

def encontrar_elemento_repetido(lista):
    if len(lista) == 0:
        return Exception
    
    for i in lista:
        if type(i) != int or type(i) != float:
            return Exception
        
    contador = {}
    for num in lista:
        if num not in contador:
            contador[num] = 1
        else:
            contador[num] += 1
    
    num_repetido = 0
    cont_repeat = 0
    cont = 0

    for i in contador:
        if contador[i] > cont_repeat and contador[i] != 1:
            num_ocorr = contador[i]
            num_repetido = i
        if contador[i] != 1:
            cont += 1

    return num_repetido if num_ocorr > cont else Exception
    
assert encontrar_elemento_repetido([]) == Exception
assert encontrar_elemento_repetido(['s', 2]) == Exception
assert encontrar_elemento_repetido(['']) == Exception
assert encontrar_elemento_repetido([1, 7,7, 9, 0, 0, 0]) == 0

print('Testes ok!')
