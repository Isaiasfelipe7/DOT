# Lista2_Questao 07. Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um outro valor dado pertence ou não à lista.


def main():

    lista = [1, 2, 7, 12, 34, 67, 22, 3, 19, 14]
    n = int(input('Digite um valor para saber se ele pertence a lista: '))

    if n in lista:
        print(f'O valor {n} pertence a lista!!!')
    else:
        print(f'O valor {n} não pertence a lista!!')
        

if __name__ == '__main__':
    main()