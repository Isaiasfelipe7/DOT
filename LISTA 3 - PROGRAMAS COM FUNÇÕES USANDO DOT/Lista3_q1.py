def volume(raio):
    if type(raio) == str:
        return Exception
    if raio <= 0:
        return Exception

    return round(4/3 * 3.14 * raio**3, 2)


assert volume(2) == 33.49, 'Deveria retornar 33.49'
assert volume(2.0) == 33.49 # Testando classe válida
assert volume('b') == Exception # Testando valor improvável
assert volume(-7) == Exception # Testando valor improvável
assert volume(4.7) == 434.67 # Testando classe válida

print('Todos testes estão ok!!')
