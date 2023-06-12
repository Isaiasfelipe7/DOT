''' Lista5_q8. Crie uma função chamada "remover_vogais" que receba uma string como parâmetro e
retorne uma nova string sem as vogais.
'''

def remover_vogais(s):
    if type(s) != str or len(s) == 0:
        return Exception
    
    s2 = ''
    for i in range(len(s)):
        if s[i] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            s2 += s[i]

    return s2

assert remover_vogais(5) == Exception
assert remover_vogais(4.8) == Exception
assert remover_vogais('I') == ''
assert remover_vogais('cd') == 'cd'
assert remover_vogais('Isaias Felipe') == 'ss Flp'
assert remover_vogais('kaisen') == 'ksn'

print('Testes ok!')
