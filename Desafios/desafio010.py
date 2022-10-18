# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# US$1,00 = R$3,27

din = float(input('Digite o valor em reais que tem em sua carteira:'))
dolar = din / 3.27
euro = din / 5.26
print('Com R${:.2f}, você consegue comprar U${:.2f} e €{:.2f}.'.format(din, dolar, euro))
