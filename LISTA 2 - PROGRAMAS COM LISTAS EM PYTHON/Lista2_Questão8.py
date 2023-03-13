# Lista2_Questão 08. Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes ocorreu a letra 'A'.

def main():

    lista = ['A', 'B', 'C', 'D', 'E', 'A', 'E', 'F', 'G', 'a', 'H', 'i', 'j', 'K', 'L', 'm', 'N', 'O', 'P', 'Q', 'R', 's', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letra = str(input('Digite uma letra para saber quantas vezes ela aparece na lista: '))
    cont = 0

    for i in lista:
        if i.upper() == letra:
            cont += 1

    print(f"A letra '{letra}', apareceu {cont} vezes na lista!")

if __name__ == '__main__':
    main()