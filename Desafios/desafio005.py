# Faça um programa que leia um número inteiro e mostre na tela o seu
# sucessor e antecessor.

num = int(input('Digite um número inteiro: '))
suc = num + 1
ant = num - 1
print('O número sucessor do {}, é {}!'.format(num, suc))
print('O número antecessor do {}, é {}!'.format(num, ant))
