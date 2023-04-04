#Lista1_Questão 14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#           S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!

def calcular_valor(n):
    cont = 1
    s = 1

    for b in range(1, n+1):
        cont *= b
        s += 1/cont

    return s

while True:
    try:
        valor_int = int(input('Informe o valor de N: '))

        valor_s = calcular_valor(valor_int)

        print(f'O Valor de S é {valor_s:.2f}')
        break
    except:
        print('Número inválido. Tente Novamente!')
