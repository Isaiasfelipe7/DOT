#Lista1_Questão 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

def somatorio(x):
    soma = 0

    for b in range(1, x+1):
        soma += b
    
    return soma

while True:
    try:
        numero = int(input('Informe um valor inteiro positivo: '))

        soma = somatorio(numero)

        print(f'O somatório de {numero} é {soma}')
        break
    except:
        print('Digite um valor inteiro. Tente Novamente.')
