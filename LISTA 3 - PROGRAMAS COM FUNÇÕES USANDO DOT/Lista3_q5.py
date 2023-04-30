def idade(anos, meses, dias):
    if type(anos) != int and anos < 0 and anos > 120 or type(meses) != int and meses < 0 or type(dias) != int and dias < 0:
        return Exception

    d_a = 365
    d_m = 30
    idd_d = (anos * d_a) + (meses * d_m) + dias

    return idd_d

assert idade(16, 7, 12) == 6062 # Testando classe válida
assert idade(19, 3, 13) == 7038 # Testando classe válida
assert idade(15, 3, 29) == 5594 # Testando classe válida
assert idade('a', 2, 6) == Exception # Testando classes inválidas
assert idade('b', 'i', 'm') == Exception # Testando inválidos
assert idade(-1, 89, 1) == Exception # Testando classes inválidas
assert idade(-7, -1, 0) == Exception # Testando classes inválidas
assert idade('a', 3, 'i') == Exception # Testando classes inválidas

print('Todos testes estão ok!!')