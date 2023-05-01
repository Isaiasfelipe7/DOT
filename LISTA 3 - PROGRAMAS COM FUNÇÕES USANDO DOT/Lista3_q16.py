import unittest
from unittest.mock import patch

def media_aritmetica():
    # Inicializa as variáveis
    soma = 0
    contador = 0

    # Loop para ler os valores
    while True:
        valor = float(input("Digite um valor positivo (ou um valor negativo para encerrar): "))
        if valor < 0:
            break
        soma += valor
        contador += 1

    # Verifica se há valores para calcular a média
    if contador == 0:
        return 0

    # Retorna a média aritmética
    return soma / contador


def teste():
    with patch('builtins.input', side_effect=['2', '3', '4', '-1']):
        assert media_aritmetica() == [3]

    with patch('builtins.input', side_effect=['8', '9', '10', '-1']):
        assert media_aritmetica() == [9]

        print('Todos testes ok!')
