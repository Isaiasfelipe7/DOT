#Lista1_Questão 06. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.

def triangulo_perimetro(lados, medida):
    p = lados * medida

    return p

def quadrado_area(lados, medida):
    a = medida ** 2

    return a

while True:
    try:
        lados_poligono =  int(input('Informe o número de lados do polígono: '))
        medida_do_lado = int(input('Informe a medida de lados: '))

        if lados_poligono == 3:
            print(f'TRIÂNGULO\nPerimetro: {triangulo_perimetro(lados_poligono, medida_do_lado)} cm')
            break
        elif lados_poligono == 4:
            print(f'QUADRADO\nÁrea: {quadrado_area(lados_poligono, medida_do_lado)} cm²')
            break
        elif lados_poligono == 5:
            print('PENTÁGONO')
            break
        else:
            print('Polígono não suportado.')
    except:
        print('Número inválido. Tente Novamente!')
