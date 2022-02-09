import math
import random
from time import time

times = []
partidas = []
quantidadeDeTimes = int(input('Digite a quantidade Total de times: '))
tabela = [['TIMES', 'PG', 'GM', 'GS', 'S', 'V', 'GA']]


def achandoValorNoarrayEAdicionandoMaisUM(array, time, valor, atributo):
    posisitonOfAtributte = 0

    for qualE in array[0]:
        for position in range(0, len(array[0])):
            if atributo == array[0][position]:
                posisitonOfAtributte = position
                
    for l in array:
        if l[0] == time:
            l[posisitonOfAtributte] = l[posisitonOfAtributte] + valor
    return array
# Inverter os valores da lista
def inverterLista(lista):
    listInvertida = []
    idx = len(lista) - 1
    while (idx >= 0 ):
        listInvertida.append(lista[idx])
        idx = idx - 1

    return listInvertida

def dadoDoTime(nome, pg, gm, cs, s, v, ga):
  dadosDostimes = [nome, pg, gm, cs, s, v, ga]
  return dadosDostimes

def tabelaDeJogos():

    linhas = len(tabela) 
    colunas = len(tabela[0]) 
    for l in range(0, linhas):
        for c in range(0, colunas):
            print(f'[{tabela[l][c]:^13}]', end='')
        print()

## Para saber a quantidade total de jogos iremos fazer uma combinação com o total de times
## agrupando de 2 em 2
## formula de combinação: N!/P!(N-P)!
quantidadeDeJogos = int((math.factorial(quantidadeDeTimes))/(math.factorial(2) * math.factorial(quantidadeDeTimes - 2)))

lista = 0
## aqui estou adicionando os nomes dos times de acorda com a quantidade
for n in range (0, quantidadeDeTimes):
    times.append(input(f'Digite o nome do {n+1}° time: '))

for n in times:
    lista = dadoDoTime(n, 0, 0, 0, 0, 0, 0)
    tabela.append(lista)
    


## verificando se a sublista já existe dentro da lista
def verificarSeExistJogos(jogos):
    timeInvertido = inverterLista(jogos)
    # print(timeInvertido)
    if  jogos in partidas:
        return True
    elif timeInvertido in partidas:
        return True
    return False
        

def qualTimeGanhou(time):
    PG = '-'
    print(time[3])
    if time[2] > time[3]:
               achandoValorNoarrayEAdicionandoMaisUM(tabela, time[0], 2, 'PG')
    elif time[2] == time[3]:
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time[0], 1, 'PG')
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time[1], 1, 'PG')

    elif time[2] < time[3]:
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time[1], 2, 'PG')


    
## nesse caso estou declarando todos os possivei  jogos
while len(partidas) < quantidadeDeJogos:
    time1 = times[random.randint(0, quantidadeDeTimes - 1)]
    time2 = times[random.randint(0, quantidadeDeTimes - 1)]

    if time1 == time2:
        continue

    
    jogos = [time1, time2]
    if verificarSeExistJogos(jogos):
        continue
    partidas.append(jogos)


for n in partidas:
    yesOrNot = input(f'A partida {n[0]} x {n[1]} já ocorreu? [S/N]')
    partida = []
    if yesOrNot == 'S':
        # colocar o placa dentro da lista
        golsDoPrimeiroTime = int(input(f'Dgitite a quantidade de gols dessa partida do time {n[0]} : '))
        golsDoSegundoTime = int(input(f'Dgitite a quantidade de gols dessa partida do time {n[1]} : '))

        n.append(golsDoPrimeiroTime)
        n.append(golsDoSegundoTime)

        


        # Colocando a quantidade de gols marcados
        achandoValorNoarrayEAdicionandoMaisUM(tabela, n[0], golsDoPrimeiroTime, 'GM')
        achandoValorNoarrayEAdicionandoMaisUM(tabela, n[1], golsDoSegundoTime, 'GM')

        # Colocando a quantidade de gols sofrindos
        achandoValorNoarrayEAdicionandoMaisUM(tabela, n[0], golsDoSegundoTime, 'GS')
        achandoValorNoarrayEAdicionandoMaisUM(tabela, n[1], golsDoPrimeiroTime, 'GS')

        print(times)
        # Colocando o número de pontos ganhos
        qualTimeGanhou(n)


print(tabela)
    

tabelaDeJogos()





