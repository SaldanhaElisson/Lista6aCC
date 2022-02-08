import math
import random

times = []
partidas = []
quantidadeDeTimes = int(input('Digite a quantidade Total de times: '))

def inverterLista(lista):
    listInvertida = []
    idx = len(lista) - 1
    while (idx >= 0 ):
        listInvertida.append(lista[idx])
        idx = idx - 1

    return listInvertida

## Para saber a quantidade total de jogos iremos fazer uma combinação com o total de times
## agrupando de 2 em 2
## formula de combinação: N!/P!(N-P)!
quantidadeDeJogos = int((math.factorial(quantidadeDeTimes))/(math.factorial(2) * math.factorial(quantidadeDeTimes - 2)))

## aqui estou adicionando os nomes dos times de acorda com a quantidade
for n in range (0, quantidadeDeTimes):
    times.append(input(f'Digite o nome do {n+1}° time: '))


## verificando se a sublista já existe dentro da lista
def verificarSeExistJogos(jogos):
    timeInvertido = inverterLista(jogos)
    # print(timeInvertido)
    if  jogos in partidas:
        # print('achei aqui')
        # print(jogos)
        # print(partidas)
        return True
    elif timeInvertido in partidas:
        print(timeInvertido)
        print(partidas)
        print('achei')
        return True
    return False
        

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


print(partidas)

## Agora irei verificar se aquela partida já aconteceu ou não
# for n in range(0, len(partidas)):
#     for a in range(0, 2):
#         yesOrNot = input()

## vou digitar a quantiade times
## depois vou calcular a quantidade de partidas por meio de combinação
## depois vou  colocar  as partidas como por exemplo: time1 x time2
    ## não pode ser time1 x time1
    ## não pode ter time1 x time2 e time2 x time1
## depois verificar se aquele jogo ocorreu com o usuario
    ## uma variavel vai  perguntar se  o jogo a x b, ocorreu e ira receber s ou n
    ## depois irá verificar a variavel, se ocorreu vai:
        ### 


### função verificar
    # vou receber a lista que quero verificar (jogos)
    # Vou criar uma variavel com lista vazia (PartidaAtual)
    # vou adicionar o ultimo item da lista enviada para essa lista vazial
    #vou inverter esse lista
    # vou verificar se a lista já existe dentro do array 
        # se sim, retorna um false
    # se não passar para proxima linha
    #vou inveter dnv a lista partidaAtual
    # vou verificar se a lista já exite dentro do array
        # se sim, retorna um false
    # se não, retorna um True

