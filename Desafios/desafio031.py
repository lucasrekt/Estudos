# Desenvolva um programa que pergunta distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

km = float(input('Quantos km de viagem serão percorridos?'))
print('Você está prestes a começar uma viagem de {}KM'.format(km))
if km <= 200:
    pkm = km * 0.50
    print('O valor da passagem ficará: R${:.2f}'.format(pkm))
else:
    pkm2 = km * 0.45
    print('O valor da passagem ficará: R${:.2f}'.format(pkm2))
