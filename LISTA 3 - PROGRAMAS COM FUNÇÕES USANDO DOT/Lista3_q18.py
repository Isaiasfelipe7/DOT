""" Lista3_q18. Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve
a tabuada de 1 até N. Mostre a tabuada na forma:
1 x N = N
2 x N = 2N
...
N x N = N2
"""

def tabuada(n):
    for i in range(1, n+1):
        for b in range(1, n+1):
            print(f'{i} x {b} = {i*b}')

tabuada(5)
