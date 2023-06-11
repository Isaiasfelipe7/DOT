''' Lista4_q5. Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
[1,3,6]
'''

def soma_cumulativa(lista):
    if len(lista) == 0:
        return Exception

    for num in lista:
        if type(num) != int:
            return Exception
    
    soma = 0
    list_cumulativa = []

    for num in lista:
        soma += num

        list_cumulativa.append(soma)
    
    return list_cumulativa 

assert soma_cumulativa([]) == Exception
assert soma_cumulativa([1.9, 2, 1]) == Exception
assert soma_cumulativa([1, 2, 3]) == [1, 3, 6]

print('Todos testes ok!')
