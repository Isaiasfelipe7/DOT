#11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

def divisores(x):
    qtd = 0 

    for i in range(1, x+1):
        if x % i == 0:
            qtd += 1

    return qtd

def main():

    num = int(input('Digite um valor inteiro positivo: '))

    quantidade = divisores(num)

    print(f'A quantidade de divisores de {num} é {quantidade}')

if __name__ == '__main__':
    main()
