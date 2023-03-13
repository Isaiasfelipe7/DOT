# Lista2_Questão 13. Tentando descobrir se um dado era viciado, um dono de um cassino honesto(ha! ha! ha!) o lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face.

def main():

    n = int(input("Digite o número de lançamentos: "))
    contagem = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for i in range(n):
        resultado = int(input(f"Digite o resultado do lançamento {i+1}: "))
        contagem[resultado] += 1

    print("O número de ocorrências de cada face foi:")
    for face, ocorrencias in contagem.items():
        print(f"Face {face}: {ocorrencias} ocorrências")

if __name__ == '__main__':
    main()