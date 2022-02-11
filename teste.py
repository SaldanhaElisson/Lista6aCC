matriz = [["Numero da conta", 1, 0, 0, 0], ["nome", 'elisson', 'daniel', 'vovo', 'saldanha'], ["Saldo", 0, 0, 0, 0]]

def achandoValorNoarrayEAdicionandoMaisUM(array, nome, valor, numero):
    posisitonOfAtributte = 0
    aux = len(array)
    for qualE in range(0, aux):
        if numero == array[0][qualE]:
            posisitonOfAtributte = qualE
                
    for l in range(0, aux):
        if array[1][l] == nome:
            print(array[2][posisitonOfAtributte])
            array[2][posisitonOfAtributte] = array[2][posisitonOfAtributte] + valor
    return array


def imprimirTabela():
    for l in range(0, 3):
        for c in range(0, 4):
            print(f'[{matriz[l][c]:^15}]', end='')
        print()

achandoValorNoarrayEAdicionandoMaisUM(matriz, 'elisson', 2, 1)

imprimirTabela()