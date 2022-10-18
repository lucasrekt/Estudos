# Escreva um programa que leia um valor em metros e o exiba convertido em
# centimetros e milímetros
m = float(input('Escreva o valor em metros:'))
cm = m * 100
mm = cm * 100
print('O valor em metros é {}m'.format(m))
print('Em centimetros {}m é igual a {}cm'.format(m, cm))
print('Em milimetros {}m é igual a {}mm'.format(m, mm))
