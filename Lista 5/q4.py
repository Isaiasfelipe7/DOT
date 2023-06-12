''' Lista5_q4. Crie uma função chamada "contar_divisores" que receba um número inteiro como
parâmetro e retorne a quantidade de divisores desse número.
'''

def contar_divisores(n):
    if type(n) != int or n <= 0:
        return Exception
    
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1

    return cont

assert contar_divisores('') == Exception
assert contar_divisores(0) == Exception
assert contar_divisores('-1') == Exception
assert contar_divisores(1) == 1
assert contar_divisores(3) == 2
assert contar_divisores(20) == 6

print('Testes ok!')
