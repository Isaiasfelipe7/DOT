#14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#           S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!

def calcular(n):
    fat = 1
    s = 1

    for i in range(1, n+1):
        fat *= i
        s += 1/fat

    return s

def main():

    num = int(input('Digite o valor de N: '))

    valor_s = calcular(num)

    print(f'O Valor de S é {valor_s}')

if __name__ == '__main__':
    main()
