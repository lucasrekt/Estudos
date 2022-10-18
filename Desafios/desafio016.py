# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
# Ex: Digite um número : 6.127
# O número 6.127 tem a parte inteira 6.

# import math
#
# num = float(input('Digite um número: '))
# print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))

# from math import trunc
# .format(num, trunc(num))

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
