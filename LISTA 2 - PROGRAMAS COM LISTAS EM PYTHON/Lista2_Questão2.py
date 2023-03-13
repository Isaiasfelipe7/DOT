# Lista2_Questão 02. Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos núemros positivos dessa lista.

def main():

    lista = []
    soma_negativo = 0
    soma_positivo = 0
    qtd_negativo = 0
    qtd_positivo = 0

    for i in range(10):
        num = float(input(f'Digite o {i+1}º número: '))
        lista.append(num)
    
    print(f'\nLISTA {lista}')

    for num in lista:
        if num < 0:
            qtd_negativo += 1
            soma_negativo += num

    print(f'\nA quantidade de números NEGATIVOS da lista é {qtd_negativo}.\ne a soma dos números negativos é {soma_negativo}')

    for num in lista:
        if num > 0:
            qtd_positivo += 1
            soma_positivo += num

    print(f'\nA quantidade de números POSITIVOS da lista é {qtd_positivo}.\ne a soma dos números positivos é {soma_positivo}')

if __name__ == '__main__':
    main()
    