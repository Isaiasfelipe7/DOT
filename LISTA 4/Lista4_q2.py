'''' Lista4_q2. Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
o número de vezes que cada número ocorre na sequência.
'''

def contar_numeros(lista):
    dic = {}

    if len(lista) == 0: # testar lista é vazia
        return Exception
    
    for num in lista:
        if type(num) != int: # testar se algum valor dav lista não é inteiro
            return Exception
        if num not in dic: # gravar quantidade de número (num) no dicionário
            dic[num] = 1
        else:
            dic[num] += 1
    return dic

assert contar_numeros([]) == Exception
assert contar_numeros(["*", 1, 2, 1]) == Exception
assert contar_numeros([5.5, 6, 5.5, 7, 9.3, 10, 9.3]) == Exception
assert contar_numeros([5, 4, 5, 7, 3, 4]) == ({5: 2, 4: 2, 7: 1, 3: 1})
assert contar_numeros([1, 3, 1, 6, 9, 6, 8, 6]) == ({1: 2, 3: 1, 6: 3, 9: 1, 8: 1})

print('Testes ok!')
