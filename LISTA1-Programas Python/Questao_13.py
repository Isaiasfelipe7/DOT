#13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.

def calcular(n):
    s = 0

    for i in range(1, n+1):
        s += 1/i

    return s

def main():

    num = int(input('Digite o valor de N: '))

    valor_s = calcular(num)

    print(f'O valor de S é {valor_s:.2f}')

if __name__ == '__main__':
    main()
