#Lista2_Questão 04. Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

def main():

    lista = []
    mai = 0
    men = 0

    for i in range(15):
        lista.append(int(input(f'Digite o valor: ')))

        if i == 0:
            mai = men = lista[i]
        else:
            if lista[i] > mai:
                mai = lista[i]
            if lista[i] < men:
                men = lista[i]

    print(f'O maior valor da lista é {mai} na posição ', end='')
    for c, v in enumerate(lista):
        if v == mai:
            print(f'{c}')

    print(f'O menor valor da lista é {men} na posição ', end='')
    for c, v in enumerate(lista):
        if v == men:
            print(f'{c}')

if __name__ == '__main__':
    main()
