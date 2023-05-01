""" Lista3_q4. Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos.
"""

def tempo(seg):
    if type(seg) != int or seg <= 0:
        return Exception
    th = seg // 3600
    tm = (seg % 3600) // 60
    ts = (seg % 3600) % 60

    return th,tm,ts

assert tempo(3600) == (1,0,0) # Testando classe válida
assert tempo(3660) == (1,1,0) # Testando classe válida
assert tempo(3661) == (1,1,1) # Testando classe válida
assert tempo(7200) == (2,0,0) # Testando classe válida
assert tempo(7320) == (2,2,0) # Testando classe válida
assert tempo(7322) == (2,2,2) # Testando classe válida
assert tempo(0) == Exception # Testando valor improvável
assert tempo(7200.4) == Exception # Testando valor improvável
assert tempo(-7) == Exception # Testando valor improvável
assert tempo('$') == Exception # Testando valor improvável
assert tempo('bim') == Exception # Testando valor improvável

print('Todos testes estão ok!')
