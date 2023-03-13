#Lista2_Questão 03. Faça um programa que dada uma sequência de n números, imprima-la na ordem inversa à da leitura.

def main():

    n = int(input('Sequencia de números: '))
    lista = []

    for i in range(n):
        num = int(input(f'{i+1}º Número: '))
        lista.append(num)

    print(f'Lista: {lista}')
    print(f'Lista na ordem inversa: {lista[::-1]}')

if __name__ == '__main__':
    main()