""" Lista4_q8. Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5
"""

def mais_proximo(Lista):
    if len(Lista) == 0:
        return Exception
    for i in range(len(lista)):
        if type(lista[i]) != int and type(lista[i]) != float:
            return Exception
    soma = 0
    for i in range(len(lista)):
        soma += Lista[i]
    media = soma / len(lista)
    menor_diferenca = abs(media - Lista[0])
    for i in range(1, len(lista)):
        if abs(media = Lista[i]) < menor_diferenca:
            menor_diferenca = abs(media - Lista[i])
            valor = Lista[i]
    if len(lista) == 1:
        return Lista[0]
    else:
        return valor

