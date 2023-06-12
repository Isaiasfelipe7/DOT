''' Lista5_q1. Crie uma função chamada "encontrar_primos_gemeos" que receba um número inteiro
n como parâmetro e retorne uma lista contendo todos os pares de números primos
gêmeos menores que n. Os números primos gêmeos são dois números primos
consecutivos que diferem em 2.
'''

def primo(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True

def encontrar_primos_gemeos(n):
    if type(n) != int or n <= 1:
        return Exception
    
    l_primos = []
    for i in range(2, n+1):
        if primo(i) == True:
            l_primos.append(i)

    l_gemeos = []
    for i in range(len(l_primos) -1):
        if l_primos[i+1] - l_primos[i] == 2:
            l_gemeos.append(l_primos[i])
            l_gemeos.append(l_primos[i+1])

    return l_gemeos

assert encontrar_primos_gemeos("*") == Exception
assert encontrar_primos_gemeos(2.5) == Exception
assert encontrar_primos_gemeos(-9) == Exception
assert encontrar_primos_gemeos(20) == [3, 5, 5, 7, 11, 13, 17, 19]

print('Testes ok!')
