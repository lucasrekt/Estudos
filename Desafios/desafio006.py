# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada;

n = int(input('Digite um número:'))
d = n * 2
t = n * 3
rq = pow(n, 1/2)
# rq = n ** (1/2) pode ser feito assim também
print('O número informado foi {}.'.format(n))
print('O dobro do número {}, é {} !'.format(n, d))
print('O triplo do número {}, é {} !'.format(n, t))
print('A raiz quadrada do número {}, é {:.2f} !'.format(n, rq))
