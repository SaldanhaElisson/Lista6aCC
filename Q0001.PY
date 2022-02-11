matriz = [["Numero da conta", 0, 0, 0, 0], ["nome", 0, 0, 0, 0], ["Saldo", 0, 0, 0, 0]]

for l in range(0, 3):
    pessoas = 0
    for c in range(1, 5):
        pessoas +=1
        if matriz[l][0] == 'Numero da conta':
            matriz[l][c] = int(input(f'{matriz[l][0]} do {pessoas}° cliente: '))
            continue

        matriz[l][c] = input(f'{matriz[l][0]} do {pessoas}° cliente: ')


def imprimirTabela():
    for l in range(0, 3):
        for c in range(0, 4):
            print(f'[{matriz[l][c]:^15}]', end='')
        print()
print('='*80)
imprimirTabela()

def achandoValorNoarrayEAdicionandoMaisUM(array, nome, valor, numero):
    posisitonOfAtributte = 0
    aux = len(array)
    for qualE in range(0, aux):
        if numero == array[0][qualE]:
            posisitonOfAtributte = qualE
                
    for l in range(0, aux):
        if array[1][l] == nome:
            array[2][posisitonOfAtributte] = float(array[2][posisitonOfAtributte]) + float(valor)
    return array

def transacao(nome, numero):
    depositarOrSacar = int(input('Digite [1] para depositar ou [0] Sacar: '))
    if depositarOrSacar == 1:
        valor = float(input('Digite o valor para depositar: '))
        achandoValorNoarrayEAdicionandoMaisUM(matriz, nome, valor, numero)
    elif depositarOrSacar == 0:
        valor = float(input('Digite o valor para sacar: '))
        achandoValorNoarrayEAdicionandoMaisUM(matriz, nome, -valor, numero)


def telaDeInicio():
    print('=' * 80)
    print()
    print('BANCO DO CC')
    print()
    print('PARA FAZER A TRANSAÇÃO COLOQUE O NOME DO CLIENTE E SEU NUMERO DA CONTA')
    print()
    print("="*80)
    login()

def login():
    numeroDaConta  = int(input('Digite o numero da conta: '))
    nomeDoUsuario = input('Digite o nome do usuario: ')
    print()

    for c in range(1, 4):
        if matriz[0][c] == numeroDaConta:
            if matriz[1][c] == nomeDoUsuario:
                nome = matriz[1][c]
                numero = matriz[0][c]
                transacao(nome, numero )
    

telaDeInicio()
print
imprimirTabela()