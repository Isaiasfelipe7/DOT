""" Lista4_q2. Escreva uma função que recebe uma lista com n números inteiros, conta e imprime o números de vezes que cada número ocorre na sequência. Obs: SEM USAR COUNT
"""

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

assert contar_numeros([19, 5.4]) == Exception
assert contar_numeros([]) == Exception
assert contar_numeros(["*", 5]) == Exception
assert contar_numeros([5, 4, 7, 3, 4, 5]) == ({3: 1, 4: 2, 5: 3, 7: 1})

print('Testes ok!')
