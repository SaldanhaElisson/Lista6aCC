tabela = [[1, 0, 0], [3, 0, 0], [1,0 ,0]]

def achandoValorNoarray(array, time, valor):
    for l in array:
        if l[0] == valor:
            l[1] = l[1] + valor
    
    return array
        

achandoValorNoarray(tabela, 1, 1)
achandoValorNoarray(tabela, 1, 1)

print(tabela)