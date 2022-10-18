# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
# from random import randint
# computador = radint(0, 5)

lista = [0, 1, 2, 3, 4, 5]
programa = random.choice(lista)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
user = int(input('Qual é o número que foi escolhido pelo programa?'))
print('Processando.....')
sleep(3)
print('O número que o programa escolheu foi: {}'.format(programa))

if user == programa:
    print('Você venceu!')
else:
    print('Você perdeu!')
