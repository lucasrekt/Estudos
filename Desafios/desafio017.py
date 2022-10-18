# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa

from math import hypot
# import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
ch = hypot(co, ca)
# ch = co ** 2 + ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(ch))
