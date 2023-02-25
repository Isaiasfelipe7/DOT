#2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
# do círculo e outra função chamada perimetro que calcula e retorna o perímetro do círculo.
#    Área = PI * r2; Perímetro = PI * 2 * r;

def area(raio):
    a = 3.14 * raio ** 2

    return a

def perimetro(raio):
    pe = 3.14 * 2 * raio

    return pe

def main():

    raio = int(input('Digite o raio do círculo : '))

    print(f'A área do circulo é: {area(raio):.2f}')
    print(f'O perímetro do círculo é: {perimetro(raio):.2f}')

if __name__ == '__main__':
    main()
