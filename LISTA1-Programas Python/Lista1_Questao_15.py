#15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... + (t^2+1)/(t+3)

def calcular_valor(valor):
    s = 0
    t = 2

    for b in range(valor):
        s += (t**2 + 1) / (t + 3)
        t += 1

    return s

def main():

    valor_int = int(input('Informe o valor de N: '))

    valor_s = calcular_valor(valor_int)

    print(f'O valor de S é {valor_s:.2f}')

if __name__ == '__main__':
    main()
