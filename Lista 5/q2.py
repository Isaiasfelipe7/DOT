''' Lista5_q2. Crie uma função chamada "verificar_anagrama" que receba duas strings como
parâmetros e retorne True se as duas strings forem anagramas (ou seja, possuírem as
mesmas letras em quantidade igual, mas em ordem diferente), e False caso contrário.
'''

def verificar_anagrama(s1, s2):
    if type(s1) != str or type(s2) != str:
        return Exception
    
    if len(s1) != len(s2):
        return Exception
    
    s1_invertida = ''
    for i in range(len(s1) -1, -1, -1):
        s1_invertida += s1[i]
    
    if s1_invertida == s2:
        return True
    else:
        return False
    
assert verificar_anagrama('ana', 55) == Exception
assert verificar_anagrama('roma', 'romario') == Exception
assert verificar_anagrama('arara', 'arara') == True
assert verificar_anagrama('amor', 'roma') == True
assert verificar_anagrama('mario', 'maria') == False

print('Testes ok!')
