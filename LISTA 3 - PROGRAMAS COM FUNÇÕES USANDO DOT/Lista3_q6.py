def perfeito(num):
    if type(num) != int:
        return Exception
    if num < 0:
        return Exception
    
    soma = 0 
    for div in range(1, num):
        if num % div == 0:
            soma += div
    if soma == num:
        return True
    else:
        return False

assert perfeito(6) == True # Testando classe válida
assert perfeito(28) == True # Testando classe válida
assert perfeito(496) == True # Testando classe válida
assert perfeito(8128) == True # Testando classe válida
assert perfeito(11) == False # Testando classe válida
assert perfeito(78) == False # Testando clase válida
assert perfeito(22) == False # Testando classe válida
assert perfeito(3) == False # Testando classe válida
assert perfeito(-1) == Exception # Testando valor improvável
assert perfeito(-3) == Exception # Testando valor improvável
assert perfeito('i') == Exception # Testando valor improvável
assert perfeito(4.7) == Exception # Testandovalor improvável

print('Todos testes estão ok!!')
