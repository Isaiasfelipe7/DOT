''' Lista5_q3. Escreva uma função chamada "contar_caracteres" que receba uma string como
parâmetro e retorne um dicionário onde as chaves são os caracteres encontrados na string
e os valores são a quantidade de ocorrências de cada caractere.
'''

def contar_caracteres(s1):
    if type(s1) != str:
        return Exception


assert contar_caracteres(2) == Exception
assert contar_caracteres(5.7) == Exception
assert contar_caracteres(-8) == Exception

print('Testes ok!')
