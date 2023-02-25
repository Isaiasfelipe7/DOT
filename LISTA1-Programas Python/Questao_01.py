#1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.

def par_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def main():

    num = int(input('Digite um número: '))

    if par_impar(num):
        print("\nO numero %d é par." %num)

    else:
        print("\nO numero %d é impar." %num)

if __name__ == '__main__':
    main()
