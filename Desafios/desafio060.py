# Calculo de fatorial:

from math import factorial

# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}.'.format(n, f))

n = int(input('Digite um número para calcular seu Fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')

while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1
print('{}'.format(f))
