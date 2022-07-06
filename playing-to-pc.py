# Programando em python

from random import randint
computador = randint(0, 10) # faz o computador escolher um numero
print('Sou seu computador... Acabei de pensar em um numeor entre 0 e 10.')
print('Será que vc consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual foi seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
           print('Mais... Tente mais uma vez.')
        elif jogador > computador:
           print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas!!'.format(palpites))
