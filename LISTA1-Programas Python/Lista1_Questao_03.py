#Lista1_Questão 03. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius.
#      Fórmula: C = ((F-32)/9)*5

def celsius(tmp):
    celsius = ((tmp - 32) / 9) * 5

    return celsius

def main():

    graus_fahremheit = float(input('Informe a temperatura em graus Fahrenheit: '))

    cels = celsius(graus_fahremheit)

    print(f'A temperatura Fahrenheit = {graus_fahremheit}, em graus Célsius é {cels:.1f}°.')


if __name__ == '__main__':
    main()
