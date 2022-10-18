n1 = input('Digite um número:')
n2 = input('Digite outro número:')
res = int(n1) + int(n2)
print('O resultado é:', res, '!')

# segunda-forma
n1 = input('Digite um número:')
n2 = input('Digite outro número:')
res = int(n1) + int(n2)
print('O resultado é {}!'.format(res))

# terceira-forma
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
print('O resultado de {} + {} é {}!'.format(n1, n2, res))
