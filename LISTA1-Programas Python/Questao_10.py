#10. Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetro de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
# b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função Max.

def Max(n1, n2):
    if n1 >= n2:
        return n1
    
    else:
        return n2

def main():

    for i in range(4):
        a1 = int(input('Primeiro número da série ' + str(i+1) + ': '))
        b1 = int(input('Segundo número da série ' + str(i+1) + ': '))
        a2 = int(input('Terceiro número da série ' + str(i+1) + ': '))
        b2 = int(input('Quarto número da série ' + str(i+1) + ': '))

        maior1 = Max(a1, b1)
        maior2 = Max(a2, b2)
        maior3 = Max(maior1, maior2)

        print(f'O maior número da série {i+1} é {maior3}')

if __name__ == '__main__':
    main()
