# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

n1 = int(input('Digite um número inteiro: '))
f = n1 % 2

if f == 0:
    print('O número {} é par!'.format(n1))
else:
    print('O número {} é impar!'.format(n1))
