# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, coss

import math

x = math.radians(float(input('Digite um valor: ')))
seno = math.sin(x)
cos = math.cos(x)
tan = math.tan(x)
print('{:.2f}'.format(seno))
print('{:.2f}'.format(cos))
print('{:.2f}'.format(tan))
