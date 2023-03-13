# Lista2_Questão 18. Ler uma lista X de 10 elementos. a seguir copiar todos os valores negativos da lista X para a lista R, sem deixar elementos vazios entre os valores copiados. escrever as listas X e R.

def main():

    X = []
    for i in range(10):
        x = int(input(f'Digite o {i+1}º elemento de X: '))
        X.append(x)

    R = []
    for x in X:
        if x < 0:
            R.append(x)

    print(f'Lista X: {X}')
    print(f'Lista R: {R}')

if __name__ == '__main__':
    main()