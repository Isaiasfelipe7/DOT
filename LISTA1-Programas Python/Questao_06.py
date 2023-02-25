#6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.

def peri_tri(lados, medida):
    perimetro = lados * medida

    return perimetro

def area_quadrado(lados, medida):
    area = medida ** 2

    return area

def main():

    lados =  int(input('Digite o número de lados do polígono: '))
    medida = int(input('Digite a medida de lados (em cm): '))

    if lados == 3:
        print(f'TRIÂNGULO\nPerimetro: {peri_tri(lados, medida)} cm')

    elif lados == 4:
        print(f'QUADRADO\nÁrea: {area_quadrado(lados, medida)} cm²')

    else:
        if lados == 5:
            print(f'PENTÁGONO')

if __name__ == '__main__':
    main()