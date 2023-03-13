# Lista2_Questão 15. Ler uma lista de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim por diante. Escrever todo a lista D e todo a lista E.


def main():

    list_D = []

    for i in range(10):
        list_D.append(int(input('Digite um valor paraa lista: ')))

        list_E = list_D[::-1]

    print(f'Lista D: {list_D}')
    print(f'Lista E: {list_E}')

if __name__ == '__main__':
    main()