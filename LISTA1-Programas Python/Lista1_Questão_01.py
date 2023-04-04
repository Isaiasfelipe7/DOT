#Lista1_Questão 01. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.

def par_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False

while True:
    try:
        num = int(input('Digite um número: '))

        if par_impar(num):
            print("\nO numero %d é par." %num)
            break
        else:
            print("\nO numero %d é impar." %num)
            break
    except:
        print('Número inváido. Tente Novamente.')
