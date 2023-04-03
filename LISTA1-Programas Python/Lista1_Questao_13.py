#Lista1_Questão 13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.

def calcular_valor(n):
    s = 0

    for b in range(1, n+1):
        s += 1/b

    return s

def main():

    while True:
        try:
            valor_int = int(input('Informe o valor de N: '))

            valor_s = calcular_valor(valor_int)

            print(f'O valor de S é {valor_s:.2f}')
            break
        except:
            print('Digite um valor inteiro. Tente Novamente.')

if __name__ == '__main__':
    main()
