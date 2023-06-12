''' Lista5_q5. Escreva uma função chamada "verificar_ano_bissexto" que receba um número inteiro
como parâmetro e retorne True se o ano for bissexto, e False caso contrário. Um ano é
bissexto se for divisível por 4, mas não divisível por 100, exceto se for divisível por 400.
'''

def verificar_ano_bissexto(n):
    if type(n) != int or n <= 3:
        return Exception
    
    if n % 4 == 0  and 100 != 0:
        return True
    elif n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
        return True
    elif n % 4 == 0 and n % 100 == 0 and n % 400 != 0:
        return False
    else:
        return False
    
assert verificar_ano_bissexto('') == Exception
assert verificar_ano_bissexto(-2032) == Exception
assert verificar_ano_bissexto(7.5) == Exception
assert verificar_ano_bissexto(2032) == True
assert verificar_ano_bissexto(2024) == True
assert verificar_ano_bissexto(2022) == False
assert verificar_ano_bissexto(1005) == False

print('Testes ok!')
