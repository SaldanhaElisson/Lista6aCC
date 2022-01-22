

from locale import MON_1, MON_11


matriz = [[ 0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print('Posições dos numeros')
print('')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{l}, {c}]', end='')
    print()
print(' ')
print(" ")
for l in range(0, 3):
    pessoas = 0
    for c in range(0, 3):
        pessoas +=1
        matriz[l][c] = int(input(f'Digite o numero da posição [{l}, {c}]: '))
print('-='*30)


# Verificando se pe um quadrado magico

primeiraLinha = 0 
segundaLinha = 0
terceiraLinha = 0

primeiraConluna = 0
segundaConluna = 0
terceiraCOnluna = 0

primeiraDiagonal = 0
segundaLinhaDiagonal = 0

rangeFor = [0, 1, 2]
gambiarra = rangeFor[:]
gambiarra.sort(reverse=True)

for m in rangeFor:
    primeiraLinha += matriz[0][m] 
    segundaLinha += matriz[1][m]
    terceiraLinha += matriz[2][m]

    primeiraConluna += matriz[m][0]
    segundaConluna += matriz[m][1]
    terceiraCOnluna += matriz[m][2]


    primeiraDiagonal += matriz[m][m]
    segundaLinhaDiagonal += matriz[m][gambiarra[m]]

