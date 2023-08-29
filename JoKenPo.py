from random import randint
from time import sleep
jogadas = ('Pedra','Papel','Tesoura')
maquina = randint(0,2)
print('''Suas opções são:
      [0] Pedra
      [1] Papel
      [2] Tesoura ''')
jogador = int(input('Qual é a sua jogada?\n'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('Máquina jogou {}'.format(jogadas[maquina]))
print('Jogador jogou {}'.format(jogadas[jogador]))
print('-='*20)

if maquina == 0 :
    if jogador ==0:
        print("EMPATE")
    elif jogador ==1:
        print("JOGADOR GANHOU")
    elif jogador ==2:
        print("MÁQUINA GANHOU")
    else:
        print('JOGADA INVÁLIDA!')
if maquina == 1 :
    if jogador ==0:
        print("MÁQUINA GANHOU")
    elif jogador ==1:
        print("EMPATE")
    elif jogador ==2:
        print("JOGADOR GANHOU")
    else:
        print('JOGADA INVÁLIDA!')
if maquina == 2 :
    if jogador ==0:
        print("JOGADOR GANHOU")
    elif jogador ==1:
        print("MÁQUINA GANHOU")
    elif jogador ==2:
        print("EMPATE")
    else:
        print('JOGADA INVÁLIDA!')