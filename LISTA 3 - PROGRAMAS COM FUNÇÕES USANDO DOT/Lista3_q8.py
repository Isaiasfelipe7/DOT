"""Lista3_q8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano.
"""

def postivo_negativo(num):
    if type(num) != int:
        return Exception
    if num >= 0:
        return True
    else:
        return False
    
assert postivo_negativo('a') == Exception
assert postivo_negativo(-2.3) == Exception
assert postivo_negativo(2.9) == Exception
assert postivo_negativo(-3) == False
assert postivo_negativo(-18) == False
assert postivo_negativo(0) == True
assert postivo_negativo(22) == True
assert postivo_negativo(152) == True
assert postivo_negativo(-7) == False

print('Todos testes ok!')
