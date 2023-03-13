# Lista2_Questão 16. Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os elementos de Y com indice par receberão os respectivos elementos de X divididos por 2; os elementos com índice ímpar receberão os respectivos elementos de X multiplicadis por 3. 
# Escrever as listas X e Y.

def main():

    X = []
    for i in range(10):
        X.append(int(input(f'Digite o {i+1}º elementos de X: ')))

    Y = []
    for i, x in enumerate(X):
        if i % 2 == 0:  
            Y.append(x/2)
        else:  
            Y.append(x*3)

    print(f'X: {X}')
    print(f'Y: {Y}')

if __name__ == '__main__':
    main()