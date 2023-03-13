# Lista2_Questão 19. Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos de S. Escrever a lista X.

def main():

    R = []
    
    for i in range(5):
        r = int(input(f'Digite o {i+1}º elemento de R: '))
        R.append(r)

    S = []

    for i in range(10):

        s = int(input(f'Digite o {i+1}º elemento de S: '))
        S.append(s)

    X = R + S

    print(f'Lista X: {X}')

if __name__ == '__main__':
    main()