matriz = [["Numero da conta", 0, 0, 0, 0], ["nome", 0, 0, 0, 0], ["Saldo", 0, 0, 0, 0]]

for l in range(0, 3):
    pessoas = 0
    for c in range(1, 5):
        pessoas +=1
        if matriz[l][0] == 'Numero da conta':
            matriz[l][c] = int(input(f'{matriz[l][0]} do {pessoas}° cliente: '))
            continue

        matriz[l][c] = input(f'{matriz[l][0]} do {pessoas}° cliente: ')
print('-='*30)

def imprimirTabela():
    for l in range(0, 3):
        for c in range(0, 4):
            print(f'[{matriz[l][c]:^15}]', end='')
        print()

imprimirTabela()

def achandoValorNoarrayEAdicionandoMaisUM(array, nome, valor, numero):
    print("elisson")
    posisitonOfAtributte = 0
    aux = len(array)
    for qualE in range(0, aux):
        if numero == array[0][qualE]:
            posisitonOfAtributte = qualE
                
    for l in range(0, aux):
        if array[1][l] == nome:
            print(array[1][posisitonOfAtributte])
            array[1][posisitonOfAtributte] = array[1][posisitonOfAtributte] + valor
    return array

def transacao(nome, numero):
    depositarOrSacar = int(input('Digite [1] para depositar ou [0] Sacar: '))
    if depositarOrSacar == 1:
        valor = int(input('Digite o valor para depositar: '))
        achandoValorNoarrayEAdicionandoMaisUM(matriz, nome, valor, numero)


def telaDeInicio():
    print('=' * 100)
    print(' CONTA DO CC')
    print()
    print(' Para entrar na conta colocaque o numero do usuario e a senha')
    print()
    login()

def login():
    numeroDaConta  = int(input('Digite o numero da conta: '))
    nomeDoUsuario = input('Digite o nome do usuario: ')

    for c in range(1, 4):
        if matriz[0][c] == numeroDaConta:
            if matriz[1][c] == nomeDoUsuario:
                nome = matriz[1][c]
                numero = matriz[0][c]
                transacao(nome, numero )
    

telaDeInicio()
imprimirTabela()