''' Lista5_q3. Escreva uma função chamada "contar_caracteres" que receba uma string como
parâmetro e retorne um dicionário onde as chaves são os caracteres encontrados na string
e os valores são a quantidade de ocorrências de cada caractere.
'''

def contar_caracteres(s1):
    if type(s1) != str:
        return Exception
    
    dic = {}
    for i in range(len(s1)):
        if s1[i] not in dic:
            dic[s1[i]] = 1
        else:
            dic[s1[i]] += 1

    return dic

assert contar_caracteres(2) == Exception
assert contar_caracteres(5.7) == Exception
assert contar_caracteres(-8) == Exception
assert contar_caracteres('Isaias') == {'I': 1, 's': 2, 'a': 2, 'i': 1}
assert contar_caracteres('ana') == {'a': 2, 'n':1}
assert contar_caracteres('programmer') == {'p': 1, 'r': 3, 'o': 1, 'g': 1, 'a': 1, 'm': 2, 'e': 1}

print('Testes ok!')
