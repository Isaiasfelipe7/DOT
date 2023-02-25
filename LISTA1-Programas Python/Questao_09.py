#9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
# no intervalo [n1, n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.

def soma_inter(n1, n2):
    soma = 0 

    for i in range(n1, n2+1):
        soma += i

    return soma

def main():

    while True:
        try:
            n1 = int(input('\nDigite o primeiro número: '))
            n2 = int(input('\nDigite o segundo número: '))

            if n1 <= n2:
                print(f'\nA soma do intervalo informado é {soma_inter(n1,n2)}')
                break
            else:
                print(f'\nn2 deve ser maior que n1. Digite novamente!')
        except:
            print(f'\nValor inválido. Digite novamente!')

if __name__ == '__main__':
    main()
