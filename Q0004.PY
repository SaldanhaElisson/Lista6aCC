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


## verificando se a sublista já existe dentro da lista
def verificar(jogos):
    partidaUnica = []
    partidaUnica.append(jogos.pop())
    if  partidaUnica in jogos:
        print(f'{partidaUnica}')
        

## nesse caso estou declarando todos os possivei  jogos
while len(partidas) < quantidadeDeJogos:
    time1 = times[random.randint(0, quantidadeDeTimes - 1)]
    time2 = times[random.randint(0, quantidadeDeTimes - 1)]

    if time1 == time2:
        continue

   

    partidas.append([time1, time2])
    verificar(partidas)

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


