def valor_inteiro(v):
    if type(v) != int:
        return Exception
    if v <= 1:
        return False
    
    for i in range(2, v):
        if v % i == 0:
            return False
    return True

assert valor_inteiro(2) == True # Testando classe válida
assert valor_inteiro(0) == False # Testando classe válida
assert valor_inteiro(-3) == False # Testando classe válida
assert valor_inteiro(1) == False # Testando classe válida
assert valor_inteiro(3) == True # Testando classe válida
assert valor_inteiro(11) == True # Testando classe válida
assert valor_inteiro(29) == True # Testando classe válida
assert valor_inteiro('bim') == Exception # Valor improvável
assert valor_inteiro(3.1) == Exception # Valor improvável
assert valor_inteiro(7.4) == Exception # Valor improvável

print('Todos testes estão ok!!')
