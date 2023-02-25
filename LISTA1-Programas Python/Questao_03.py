#3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar 
# o valor correspondente em graus Celsius.
#      Fórmula: C = ((F-32)/9)*5

def celsius(temperatura):
    cel = ((temperatura - 32) / 9) * 5

    return cel

def main():

    temp_fahrenheit = float(input('Insira a temperatura em graus Fahrenheit: '))

    print(f'O valor correspondente da temperatura Fahreheit {temp_fahrenheit} em graus Celsius é {celsius(temp_fahrenheit):.1f}°')


if __name__ == '__main__':
    main()
