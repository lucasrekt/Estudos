# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostra uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade do carro?'))

if vel > 80:
    print('Você foi multado!\n'
          'A multa é um total dê: R${:.2f}'.format(vel * 7 - 560))
    # (vel - 80) * 7
else:
    print('Você não foi multado :)')
