# lista2_Questão 05. Faça um programa que leia duas listas de 10 elementos númericos cada e intercale os elementos deste em uma outra lista de 20 elementos cada.

def main():

    lista1 = []
    lista2 = []

    for i in range(10):
        lista1.append(int(input('Digite um valor para a primeira lista: ')))

    for c in range(10):
        lista2.append(int(input('Digite um valor para a segunda lista: ')))

    lista3 = lista1 + lista2

    lista3[::2] = lista1
    lista3[1::2] = lista2

    print(f'Lista 1: {lista1}')
    print(f'Lista 2: {lista2}')
    print(f'Lista 3 intercalada: {lista3}')

if __name__ == '__main__':
    main()