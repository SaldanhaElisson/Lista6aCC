matriz = [["NUmero da conta", 0, 0, 0, 0], ["nome", 0, 0, 0, 0], ["OP", 0, 0, 0, 0], ["salario", 0, 0, 0, 0], ["op", 0, 0, 0, 0]]

for l in range(0, 5):
    pessoas = 0
    for c in range(1, 5):
        pessoas +=1
        matriz[l][c] = input(f'{matriz[l][0]} do {pessoas}° cliente: ')
print('-='*30)

for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]:^15}]', end='')
    print()