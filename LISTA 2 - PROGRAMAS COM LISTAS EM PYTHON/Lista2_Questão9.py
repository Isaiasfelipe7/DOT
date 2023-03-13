# Lista2_Questão 09. Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.


def main():

    list_x = []

    for i in range(5):
        list_x.append(int(input('Digite um valor para a lista X: ')))

    list_y = list_x[::-1]

    print(f'Lista X: {list_x}')
    print(f'Lista Y: {list_y}')

if __name__ == '__main__':
    main()