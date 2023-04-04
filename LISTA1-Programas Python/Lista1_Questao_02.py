#Lista1_Questão 02. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
# do círculo e outra função chamada perimetro que calcula e retorna o perímetro do círculo.
#    Área = PI * r2; Perímetro = PI * 2 * r;

def Area(raio):
    area = 3.14 * raio ** 2

    return area

def Perimetro(raio):
    perimetro = 3.14 * 2 * raio

    return perimetro

while True:
    try:
        raio_circulo = int(input('Digite o raio do círculo : '))

        print(f'A área do circulo é {Area(raio_circulo):.2f}')
        print(f'O perímetro do círculo é {Perimetro(raio_circulo):.2f}')
        break
    except:
        print('Número inválido. Tente Novamente!')
