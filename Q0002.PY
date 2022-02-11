matriz = [["Matricula", "nome", "função", "salario"], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]

pessoas = 0
for l in range(1, 5):
    pessoas += 1
    for c in range(0, 4):
        if matriz[0][c] == "salario":
            matriz[l][c] = float(input(f'{matriz[0][c]} do {pessoas}° funcionario: '))
            print()
            continue
        matriz[l][c] = input(f'{matriz[0][c]} do {pessoas}° funcionario: ')
print('='*50)

for l in range(0, 5):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^15}]', end='')
    print()

maiorSalario = 0
pessoaDoMaiorSalario = ""

for m in range(1, 4):
    if maiorSalario < matriz[m][3]:
        maiorSalario = matriz[m][3] 
        pessoaDoMaiorSalario = matriz[m][1]

print(f'O funcionario {pessoaDoMaiorSalario} tem o maior salario de {maiorSalario}')

