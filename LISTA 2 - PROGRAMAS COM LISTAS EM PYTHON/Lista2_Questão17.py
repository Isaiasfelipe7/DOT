# Lista2_Questão 17. Ler uma lista W elementos, depois ler um valor V. Contar e escrever quantas vezes o valor V ocorre na lista W e escrever também em que posições(indices) da lista W o valor V aparece.


def main():

    W = []
    for i in range(10):
        w = int(input(f'Digite o {i+1}º elemento de W: '))
        W.append(w)

    V = int(input('Digite o valor V: '))

    ocorrencias = 0
    indic = []
    for i, w in enumerate(W):
        if w == V:
            ocorrencias += 1
            indic.append(i)

    if ocorrencias == 0:
        print(f'O valor V não ocorre na lista W.')
        
    else:
        print(f'O valor V ocorre {ocorrencias} vezes na lista W.')
        print(f'O valor V ocorre nas posições (índices) {indic}.')

if __name__ == '__main__':
    main()
