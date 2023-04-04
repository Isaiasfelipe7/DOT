#Lista1_Questão 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

def divisores(x):
    quantidade = 0 

    for i in range(1, x+1):
        if x % i == 0:
            quantidade += 1

    return quantidade

while True:
    try:
        valor_int = int(input('Digite um valor inteiro positivo: '))

        quantidade = divisores(valor_int)

        print(f'A quantidade de divisores de {valor_int} é {quantidade}')
        break
    except:
        print('Digite um valor inteiro. Tente Novamente')
