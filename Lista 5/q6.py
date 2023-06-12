''' Lista5_q6. Crie uma função chamada "contar_substrings" que receba uma string e uma substring
como parâmetros e retorne a quantidade de ocorrências da substring na string.
'''

def contar_substrings(strin, subs):
    if type(strin)!= str or type(subs) != str:
        return Exception
    
    if len(strin) == 0 or len(subs) == 0:
        return Exception

    contador = 0
    tamanho_substring = len(subs)
    tamanho_string = len(strin)
    
    for i in range(tamanho_string - tamanho_substring + 1):
        if strin[i:i+tamanho_substring] == subs:
            contador += 1
    
    return contador

assert contar_substrings(2, 'y') == Exception
assert contar_substrings('x', 5) == Exception
assert contar_substrings('', 'in') == Exception
assert contar_substrings('banana', 'an') == 2
assert contar_substrings('abracadabra' , 'abra') == 2

print('Testes ok!')
