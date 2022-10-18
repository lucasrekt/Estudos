# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999. No final, mostre quantos números foram digitados e qual foi a entre eles.

s = n = c = 0

while n != 999:
    s += n
    n = int(input('Digite um número [999 para parar]: '))
    c += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(c - 1, s))
