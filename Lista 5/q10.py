''' Lista5_q10. Escreva uma função chamada "verificar_quadrado_perfeito" que receba um número
inteiro como parâmetro e retorne True se o número for um quadrado perfeito, e False
caso contrário. Um número inteiro é considerado um quadrado perfeito quando ele é o
resultado da multiplicação de um número inteiro por ele mesmo. Em outras palavras, um
número inteiro "n" é um quadrado perfeito se existir um número inteiro "m" tal que "n =
m * m". Por exemplo, os números 4, 9, 16 e 25 são quadrados perfeitos, pois podem ser
obtidos pela multiplicação de um número inteiro por ele mesmo: 4 = 2 * 2; 9 = 3 * 3; 16 =
4 * 4; 25 = 5 * 5.
Obs: não utilizar a função raiz quadrada isqrt().
'''

def verificar_quadadro_perfeito(num):
    if type(num) != int or num < 0:
        return Exception
    
    m = int(num ** (1/2))
    if num == m * m:
        return True
    else:
        return False
    

assert verificar_quadadro_perfeito(-4) == Exception
assert verificar_quadadro_perfeito(3.7) == Exception
assert verificar_quadadro_perfeito('y')  == Exception
assert verificar_quadadro_perfeito([]) == Exception
assert verificar_quadadro_perfeito(4) == True
assert verificar_quadadro_perfeito(9) == True
assert verificar_quadadro_perfeito(16) == True
assert verificar_quadadro_perfeito(25) == True
assert verificar_quadadro_perfeito(2) == False
assert verificar_quadadro_perfeito(3) == False
assert verificar_quadadro_perfeito(4) == True
assert verificar_quadadro_perfeito(6) == False

print('Testes ok!')

    