#12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

def somatorio(x):
    soma = 0

    for i in range(1, x+1):
        soma += i
    
    return soma

def main():

    num = int(input('Digite um valor inteiro positivo: '))

    soma = somatorio(num)

    print(f'O somatório de {num} é {soma}')

if __name__ == '__main__':
    main()
