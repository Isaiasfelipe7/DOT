# Lista2_Questão 11. Faça um programa que alimente uma lista com um número de posições definidas pelo usuário.

# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# ==== =MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 0) Sair do programa
# ——————–
# Digite sua escolha:_


def nomes(lista):
    nome = str(input('Digite o nome a ser cadastrado: ').lower())
    lista.append(nome)

    print('\nNome Cadastrado com Sucesso!!')

def encontrar_nome(lista):
    nome = str(input('Nome a ser encontrado: ').lower())

    if nome in lista:
        print(f'\nO nome {nome}, foi encontrado na lista.')
    
    else:
        print(f'\nO nome {nome}, não encontrado na lista.')

def listar_nomes(lista):
    print('\nLista de nomes:')

    for nome in lista:
        print(f'{nome}')


def main():

    lista = []

    while True:
        print('''\n=== =MENU========
1) Cadastrar nome
2) Pesquisar nome
3) Listar todos os nomes
0) Sair do programa

        ''')

        escolha = int(input('Digite sua escolha: '))

        if escolha == 1:
            nomes(lista)

        elif escolha == 2:
            encontrar_nome(lista)
        
        elif escolha == 3:
            listar_nomes(lista)

        elif escolha == 0:
            print('\nPrograma Encerrado!!')
            break

        else:
            print('\nOpção inválida, Tente Novamente.')

if __name__ == '__main__':
    main()
