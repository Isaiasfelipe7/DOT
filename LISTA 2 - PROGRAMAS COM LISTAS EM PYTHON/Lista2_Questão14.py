# Lista2_Questão 14. Ler uma lista de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
# Escrever a lista C modificada.

def main():

    listaC = []

    for i in range(10):
        listaC.append(int(input('Digite um valor: ')))

        if listaC[i] < 0:
            listaC[i] = 0

    print(f'Lista C modificada: {listaC}')

if __name__ == '__main__':
    main()
