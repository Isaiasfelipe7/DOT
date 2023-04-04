#Lista1_Questão 07. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!;e, assim por diante, até que N seja 1, quando entao tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrad o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro.

def fatorial(f):
    fat = 1

    for i in range(1, f+1):
        fat += i

    return fat

while True:
    try:
        num = int(input('Digite um número para saber seu fatorial: '))

        fat = fatorial(num)

        print(f'O Fatorial de {num} é: {fat}')
        break
    except:
        print('Número inválido. Tente Novamente!')
