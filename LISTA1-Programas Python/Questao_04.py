#Litsa1_Questão 04. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas 
# notas por parâmetro e calcule e escreva a média semestral e a mensagem "PARABÉNS! Você foi aprovado!" somente se o aluno
# foi aprovado (considere 6.0 a média mínima para aprovação).


def nota_avaliaçoes(n1, n2):
    med = (n1 + n2) / 2

    return med

def main():

    nota1 = float(input('Informe a Primeira nota: '))
    nota2 = float(input('Informe a Segunda nota: '))

    media = nota_avaliaçoes(nota1, nota2)

    if media >= 6.0:
        print(f'Sua média semestral é {media:.1f}\nPARABÉNS! Você foi aprovado!')

    else:
        print(f'Sua média semestral é {media:.1f}')

if __name__ == '__main__':
    main()