#Lista_Questão 08. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até que o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def caractere():
    while True :
        resposta = str(input("Digite 'S' para Sim ou 'N' para Não: ").upper())
        if resposta == 'S' or resposta == 'N':
            return resposta
        else:
            print(f'Caractere inválido. Digite novamente.')

def main():

    while True:
        numero = float(input('Informe o número: '))
        cubo = numero ** 3
        print(f'O número {numero:.0f} ao cubo é {cubo}')

        conti = caractere()

        if conti ==  'N':
            break

if __name__ == '__main__':
    main()