def contar_ocorrencias(lista):
    ocorrencias = {}
    
    for numero in lista:
        encontrado = False
        for chave in ocorrencias:
            if chave == numero:
                ocorrencias[chave] += 1
                encontrado = True
        if not encontrado:
            ocorrencias[numero] = 1
    
    for chave in ocorrencias:
        quantidade = ocorrencias[chave]
    
    return quantidade

assert contar_ocorrencias([5, 4, 5, 7, 3, 4]) == 2

print('Testes ok!')
