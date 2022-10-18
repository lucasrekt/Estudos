# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para
# pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Qual a largura da sua parede?'))
h = float(input('E a altura?'))
a = larg * h
t = a / 2
print('A área da sua parede é: {}m²'.format(a))
print('Para pintar a parede, será necessário {}L de tinta'.format(t))
