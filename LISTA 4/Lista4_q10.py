''' Lista4_q10. Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3,
10, 3, 1] = 20
'''

def maior_soma(lista):
    dic = {}
    if len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    soma = 0
    for num in dic:
        if dic[num] > 1:
            if dic[num] * num > soma:
                soma = dic[num] * num
    return soma

assert maior_soma([]) == Exception
assert maior_soma(["*", 2, 3]) == Exception
assert maior_soma([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]) == 20
assert maior_soma([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 16

print('Testes ok!')
