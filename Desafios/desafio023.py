# Faça um programa que leia um número de 0 a 9999 e mostra na tela cada um dos digitos separados.
# Ex:
# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um número de 0 a 9999: '))
# print('Unidade: ', num[3])
# print('Dezena: ', num[2])
# print('Centena: ', num[1])
# print('Milhar: ', num[0])
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
