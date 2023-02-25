#15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... + (t^2+1)/(t+3)

def calcular(n):
    s = 0
    t = 2

    for i in range(n):
        s += (t**2 + 1) / (t + 3)
        t += 1

    return s

def main():

    num = int(input('Digite o valor de N: '))

    valor_s = calcular(num)

    print(f'O valor de S é {valor_s}')

if __name__ == '__main__':
    main()
