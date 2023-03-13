#Lista2_Questão 01. Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com números ímpares e mostre a lista.

def main():

    listap = []
    listai = []
    qtd_par = 0
    qtd_impar = 0

    for i in range(1, 100+1):
        if i % 2 == 0:
            qtd_par += 1
            listap.append(i)

    print(f'{qtd_par}\n{listap}')
            
    for i in range(1, 100+1):
        if i % 2 == 1:
            qtd_impar += 1
            listai.append(i)

    print(f'{qtd_impar}\n{listai}')

if __name__ == '__main__':
    main()
    