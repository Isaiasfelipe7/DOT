""" Lista3_q9. Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano.
"""

def par_impar(num):
    if type(num) != int or num <= 0:
        return Exception
    if num % 2 == 0:
        return True
    else:
        return False

assert par_impar(2) == True
assert par_impar(4) == True
assert par_impar(14) == True
assert par_impar(256) == True
assert par_impar(68) == True
assert par_impar(3) == False
assert par_impar(15) == False
assert par_impar(367) == False
assert par_impar('a') == Exception
assert par_impar(-2.7) == Exception
assert par_impar(4.7) == Exception
assert par_impar(0) == Exception
assert par_impar(-7) == Exception
assert par_impar('fear') == Exception

print('Todos testes ok!')
