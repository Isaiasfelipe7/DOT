#5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
# que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
#      - para Homens: (72.7 * h) - 58
#      - para Mulheres: (62.1 * h) - 44.7
#      - Observação: Altura = h (na fórmula acima).

def peso_ideal(altura, sexo):
    if sexo == 1:
        peso_ideal = (62.1 * altura) - 44.7
    elif sexo == 2:
        peso_ideal = (72.7 * altura) - 58

    return peso_ideal

def main():

    altura = float(input('Digite sua altura: '))
    sexo = int(input('Digite seu sexo (1 para Feminino e 2 para Masculino): '))

    peso = peso_ideal(altura, sexo)

    print(f'O seu peso ideal é {peso:.2f} kg')

if __name__ == '__main__':
    main()
