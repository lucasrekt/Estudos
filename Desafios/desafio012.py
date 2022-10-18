# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

p = float(input('Qual o preço do produto?'))
vd = p * (5 / 100)
vf = p - vd
print('Com o desconto de 5% diminui: R${:.2f}'.format(vd))
print('O preço final é: R${:.2f}'.format(vf))
