# Lista2_Questão 12. Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma; 
# o cartão de respostas para cada aluno, contendo o seu número e suas repostas.

def main():

    gabarito = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']

    respostas_alunos = [
        {'numero': 1, 'respostas': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']},
        {'numero': 2, 'respostas': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'D']},
        {'numero': 3, 'respostas': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'C']}
    ]

    def calcular_acertos(respostas_aluno):
        acertos = 0
        for i in range(30):
            if respostas_aluno[i] == gabarito[i]:
                acertos += 1
        return acertos

    for aluno in respostas_alunos:
        numero_acertos = calcular_acertos(aluno['respostas'])
        print(f"Aluno {aluno['numero']}: {numero_acertos} acertos")


if __name__ == '__main__':
    main()
