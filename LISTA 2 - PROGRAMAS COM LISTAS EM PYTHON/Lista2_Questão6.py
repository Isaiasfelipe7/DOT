# Lista2_Questão 06. Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba o faturamento total que é o somatório de todos faturamentos, a média dos faturamentos e quantos faturamentos estão abaixo da média.

def main():

    lista1_qtd = []
    lista2_preco = []

    fatura = []

    for i in range(len(lista1_qtd)):
        fatura.append(lista1_qtd[i] * lista2_preco[i])

    faturamento_tot = sum(fatura)
    media_fatur = faturamento_tot / len(fatura)

    fatur_abaixo_media = 0

    for f in fatura:
        if f < media_fatur:
            fatur_abaixo_media += 1

    print(f'O faturamentto total foi R$ {faturamento_tot:.2f}')
    print(f'A média dos faturamentos é de {media_fatur:.2f}')
    print(f'{fatur_abaixo_media} faturamentos estão abaixo da média.')


if __name__ == '__main__':
    main()