import math
import random

times = []
partidas = []
quantidadeDeTimes = int(input('Digite a quantidade Total de times: '))

## Para saber a quantidade total de jogos iremos fazer uma combinação com o total de times
## agrupando de 2 em 2
## formula de combinação: N!/P!(N-P)!
quantidadeDeJogos = int((math.factorial(quantidadeDeTimes))/(math.factorial(2) * math.factorial(quantidadeDeTimes - 2)))

## aqui estou adicionando os nomes dos times de acorda com a quantidade
for n in range (0, quantidadeDeTimes):
    times.append(input(f'Digite o nome do {n+1}° time: '))


## nesse caso estou declarando todos os possivei  jogos
while len(partidas) < quantidadeDeJogos:
    time1 = times[random.randint(0, quantidadeDeTimes - 1)]
    time2 = times[random.randint(0, quantidadeDeTimes - 1)]

    if time1 == time2:
        continue

    if [time1, time2] in partidas:
        continue

    partidas.append([time1, time2])

## Agora irei verificar se aquela partida já aconteceu ou não
for n in range(0, len(partidas)):
    for a in range(0, 2):
        yesOrNot = input()
    



