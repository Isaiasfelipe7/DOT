# Lista2_Questão 10. Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemeto se encontra.


def main():

    lista = []
    maior = 0
    menor = 0

    for i in range(15):
        lista.append(int(input('Digite um valor para a lista: ')))

        if i == 0:
            maior = menor = lista[i]
        
        else:
            if lista[i] > maior:
                maior = lista[i]
            if lista[i] < menor:
                menor = lista[i]

    print(f'O maior elemento da lista é {maior}, na posição ', end='')
    for c, v in enumerate(lista):
        if v == maior:
            print(f'{c}.')

    print(f'O menor elemento da lista é {menor}, na posição ', end='')
    for c, v in enumerate(lista):
        if v == menor:
            print(f'{c}.')

if __name__ == '__main__':
    main()